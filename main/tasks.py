import random
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import Subscriber, Fact
from main.utils import send_daily_email, send_no_more_facts_email


@shared_task
def send_daily_email_task():
    subscribers = Subscriber.objects.filter(is_active=True)
    for subscriber in subscribers:
        related_facts = Fact.objects.filter(animal=subscriber.subscribed_to)
        unreceived_facts = related_facts.exclude(pk__in=subscriber.received_fact_ids.all())
        if unreceived_facts.exists():
            random_unreceived_fact = random.choice(unreceived_facts)
            send_daily_email(subscriber, random_unreceived_fact)

        else:
            subscriber.is_active = False
            send_no_more_facts_email(subscriber)

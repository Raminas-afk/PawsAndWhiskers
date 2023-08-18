import random
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import Subscriber, Fact
from main.utils import send_daily_email


# @shared_task
# def send_daily_email_task():
#     subscriber = Subscriber.objects.filter(email='raminasceponis7@gmail.com').first()
#     subject = 'Paws and Whiskers: Your Daily Fact'
#     message = 'celery works'
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [subscriber.email]
#     send_mail(subject, message, from_email, recipient_list)
#

@shared_task
def send_daily_email_task():
    subscribers = Subscriber.objects.filter(is_active=True)
    for subscriber in subscribers:
        related_facts = Fact.objects.filter(animal=subscriber.subscribed_to)
        random_fact = random.choice(related_facts)
        send_daily_email(subscriber, random_fact)

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import Subscriber


@shared_task
def send_daily_email_task():

    subscriber = Subscriber.objects.filter(email='raminasceponis7@gmail.com').first()
    subject = 'Paws and Whiskers: Your Daily Fact'
    message = 'celery works'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [subscriber.email]
    send_mail(subject, message, from_email, recipient_list)


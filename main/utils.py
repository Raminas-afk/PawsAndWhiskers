from django.conf import settings
from django.core.mail import send_mail


def send_confirmation_email(email, animal_object):
    subject = 'Paws and Whiskers confirmation email'
    message = (f'Thank you for subscribing to Paws and Whiskers! Starting today you will receive daily facts about '
               f'your favourite animal - {animal_object.name} !')
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def send_daily_email(subscriber, fact):
    subject = f'Paws and Whiskers: Daily fact about {subscriber.subscribed_to} !'
    message = fact.text
    email = subscriber.email
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

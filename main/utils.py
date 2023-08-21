from django.conf import settings
from django.core.mail import send_mail


# def send_subscription_successful_email(email, animal_object):
#     subject = 'Paws and Whiskers confirmation email'
#     message = (f'Thank you for subscribing to Paws and Whiskers! Starting today you will receive daily facts about '
#                f'your favourite animal - {animal_object.name} !')
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message, from_email, recipient_list)


def send_confirmation_email(subscriber):
    subject = 'Confirm Your Subscription to Paws and Whiskers'
    message = f'''

Thank you for subscribing to Paws and Whiskers, your source for daily animal facts and fun! We're excited to have you on board.

To confirm your subscription and start receiving facts about {subscriber.subscribed_to}s, please click on the link below:

Confirmation Link: https://127.0.0.1:8000/confirm/{subscriber.confirmation_token}

If you didn't request this subscription, you can safely ignore this email.

Best regards,
The Paws and Whiskers Team
'''
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [subscriber.email]
    send_mail(subject, message, from_email, recipient_list)


def send_daily_email(subscriber, fact):
    subject = f'Paws and Whiskers: Daily fact about {subscriber.subscribed_to} !'
    message = fact.text
    email = subscriber.email
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def send_no_more_facts_email(subscriber):
    subject = 'No More Facts Available for Your Selected Animal'
    message = f'''
    
We're sorry to inform you that there are currently no more available facts about {subscriber.subscribed_to}s.
It seems we've shared all the fascinating facts we have for this animal.

Don't worry though! There are plenty of other amazing animals waiting to be discovered. You can update your subscription preferences to receive facts about a different animal or cancel the subscription.

If you have any questions or concerns, please don't hesitate to contact us.

Best regards,
The Paws and Whiskers Team
'''
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [subscriber.email]
    send_mail(subject, message, from_email, recipient_list)

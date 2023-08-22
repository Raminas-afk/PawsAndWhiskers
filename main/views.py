from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


from .models import Subscriber, Animal

from .utils import send_confirmation_email


def front_page(request):
    available_animals = Animal.objects.all()
    return render(request, 'main.html', {'available_animals': available_animals})


def thank_you_page(request, token=None):
    if not token:
        return redirect('front-page')
    try:
        Subscriber.objects.get(confirmation_token=token)
        return render(request, 'thank_you.html')
    except ObjectDoesNotExist:
        messages.error(request, 'Confirmation link is expired or invalid')
        return redirect('front-page')


def subscribe_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        animal_name = request.POST['animal']
        animal_name = animal_name.capitalize()
        animal_object = Animal.objects.filter(name=animal_name).first()

        subscriber_exists = Subscriber.objects.filter(email=email).exists()
        if subscriber_exists:
            error_message = 'Email already subscribed'
            messages.error(request, error_message)
            return redirect('front-page')

        subscriber = Subscriber.objects.create(email=email, subscribed_to=animal_object)
        send_confirmation_email(subscriber)
        messages.success(request, f'Confirmation email sent to {email}')
        return redirect('front-page')


def confirm_email_view(request, token):
    subscriber = Subscriber.objects.filter(confirmation_token=token).first()
    if not subscriber:
        messages.error(request, 'Confirmation link is expired or invalid')
        return redirect('front-page')
    else:
        subscriber.is_active = True
        subscriber.save()
    return redirect('thank-you', token)


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
from .models import Subscriber, Animal
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import send_confirmation_email


def front_page(request):
    available_animals = Animal.objects.all()
    return render(request, 'main.html', {'available_animals': available_animals})


def thank_you_page(request):
    return render(request, 'thank_you.html')


def subscribe_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        animal_name = request.POST['animal']
        animal_name = animal_name.capitalize()
        animal_object = Animal.objects.filter(name=animal_name).first()

        email_exists = Subscriber.objects.filter(email=email).exists()
        if email_exists:
            error_message = 'Email already subscribed'
            messages.error(request, error_message)
            return redirect('front-page')

        Subscriber.objects.create(email=email, subscribed_to=animal_object)
        send_confirmation_email(email, animal_object)
        return redirect('thank-you')



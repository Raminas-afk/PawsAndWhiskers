from django.contrib import admin
from django.urls import path, include
from main.views import front_page, subscribe_view, thank_you_page, confirm_email_view

urlpatterns = [
    path('', front_page, name='front-page'),
    path('subscribe/', subscribe_view, name='subscribe'),
    path('confirm/<str:token>/', confirm_email_view, name='confirm-email'),
    path('thank-you/', thank_you_page, name='thank-you'),
]
from django.contrib import admin
from django.urls import path, include
from main.views import front_page, subscribe_view, thank_you_page

urlpatterns = [
    path('', front_page, name='front-page'),
    path('subscribe/', subscribe_view, name='subscribe'),
    path('thank-you/', thank_you_page, name='thank-you'),
]
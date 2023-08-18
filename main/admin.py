from django.contrib import admin
from .models import Subscriber, Animal, Fact

# Register your models here.

admin.site.register(Animal)
admin.site.register(Fact)
admin.site.register(Subscriber)

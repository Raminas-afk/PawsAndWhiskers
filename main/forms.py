from django import forms
from .models import Subscriber


class SubscribeForm(forms.ModelForm):
    def __init__(self, *args, animal_choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        if animal_choices is not None:
            self.fields['subscribed_to'].queryset = animal_choices

    class Meta:
        model = Subscriber
        fields = ['email', 'subscribed_to']

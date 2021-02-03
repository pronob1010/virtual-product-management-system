from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import customer_input

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)

class customer_input_form(forms.ModelForm):
    class Meta:
        model = customer_input
        exclude = ('customer','product','order_price','order_time')
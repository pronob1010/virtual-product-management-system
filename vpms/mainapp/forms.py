from django import forms
from .models import customer_input

class customer_input_form(forms.ModelForm):
    class Meta:
        model = customer_input
        exclude = ('customer','product','order_price','order_time')
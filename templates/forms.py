# forms.py
from django import forms

class PhoneNumberRegistrationForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label='Mobile Number')

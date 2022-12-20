from django.contrib import admin
from django import forms
from .models import Account
from django.core.exceptions import ValidationError
class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password' ,widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields= ('phone_number' , 'lastname', 'firstname')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dont match')
        return cd['password2']

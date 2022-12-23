from django import forms
from .models import Account
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('phone_number', 'lastname', 'firstname')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dont match')
        return cd['password2']

    def save(self, commit: True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text='you cant change password using <a href = \'../password/\'></a>')

    class Meta:
        model = Account
        fields = ('phone_number', 'lastname', 'firstname', 'last_login')


class RegistrationForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    firstname = forms.CharField(max_length='100', label='First name')
    lastname = forms.CharField(max_length='100', label='Last name')
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)

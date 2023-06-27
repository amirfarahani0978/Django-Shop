from django import forms


class Contact(forms.Form):
    comment = forms.CharField()
    name = forms.CharField()
    email = forms.CharField()
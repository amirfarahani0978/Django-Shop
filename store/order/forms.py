from django import forms


class CartAddForm(forms.Form):
    quantity = forms.P(min_value=1 ,widget=forms.NumberInput(attrs={'class': 'form-control rounded'}))


class OfferForm(forms.Form):
    code = forms.CharField()

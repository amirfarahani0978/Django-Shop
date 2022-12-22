from django.shortcuts import render
from django.contrib import admin
from django.views import View
from .forms import RegistrationForm


class RegisterView(View):
    form_class = RegistrationForm
    def get(self, request):
        form = self.form_class
        return render(request , 'account/register.html' , {'form': form})

    def post(self, request):
        pass

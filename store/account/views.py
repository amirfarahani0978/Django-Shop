from django.shortcuts import render, redirect
from django.contrib import admin
from django.views import View
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.contrib.auth import logout as auth_logout


class RegisterView(View):
    form_class = RegistrationForm
    def get(self, request):
        form = self.form_class
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Account.objects.create(
                phone_number=cd['phone_number'], firstname=cd['firstname'], lastname=cd['lastname'], password=cd['password'])
            messages.success(request, "your login successfully!!!")
            return redirect('home:home')
        return render(request, 'home:home', {'form': form})


class LogOutView(View):
    def get(self, request):
        auth_logout(request)
        messages.info(request , 'logout successfully !!!' , 'info')
        return redirect('home:home')

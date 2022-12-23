from django.shortcuts import render, redirect
from django.contrib import admin
from django.views import View
from .forms import RegistrationForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate
from .models import Account
from django.contrib import messages
from django.contrib.auth import login as auth_login
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
            Account.objects.create_user(
                phone_number=cd['phone_number'], firstname=cd['firstname'], lastname=cd['lastname'], password=cd['password'])
            messages.success(request, "your Signup successfully!!!")
            return redirect('home:home')
        return render(request, 'home:home', {'form': form})


class LoginView(View):
    form_class = LoginForm

    def get(self, request):
        form = self.form_class
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            account = authenticate(
                request, phone_number=cd['phone_number'], password=cd['password'])
            if account is not None:
                auth_login(request, account)
                messages.success(
                    request, 'Login is successfully !!!', 'success')
                return redirect('home:home')
            else:
                messages.error(
                    request, "Phone number or password is not correct ?", 'danger')
                return redirect('home:home')


class LogOutView(View):
    def get(self, request):
        auth_logout(request)
        messages.info(request, 'logout successfully !!!', 'info')
        return redirect('home:home')


class UpdateAccount(View):
    def get(self , request , phone_number):
        account = Account.objects.get(phone_number=phone_number)
        form = ProfileForm()
        return render(request , 'account/profile.html' , {'form':form})
    # def post(self, request , phone_number):
    #     account = Account.objects.get(phone_number=phone_number)
    #     form = ProfileForm(request.POST, instance = account)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request , 'This user update', 'success')
    #         return redirect('home:home')
class ProfileView(View):
    def get(self , request , user_id):
        user = Account.objects.get(id = user_id)
        return render(request , 'account/profile.html' , {'user':user})
from django.shortcuts import render, redirect
from django.contrib import admin
from django.views import View
from .forms import RegistrationForm, LoginForm, ProfileForm , VerfiyCodeForm
from django.contrib.auth import authenticate
from .models import Account , OtpCode
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from utils import send_otp_code
import random
from order.models import Order
class RegisterView(View):
    form_class = RegistrationForm
    template_name = 'account/register.html'
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            rand = random.randint(1000 , 9999)
            send_otp_code(cd['phone_number'] , rand)
            OtpCode.objects.create(phone_number = cd['phone_number'] , code = rand)
            request.session['user_registration_info'] = {
                'phone_number' : cd['phone_number'] , 
                'firstname': cd['firstname'],
                'lastname':cd['lastname'],
                'password':cd['password']
            }
            # Account.objects.create_user(
            #     phone_number=cd['phone_number'], firstname=cd['firstname'], lastname=cd['lastname'], password=cd['password'])
            messages.success(request, 'we sent you a code' , 'success')
            return redirect('register:verifycode')
        return render(request , 'account/register.html',{'form':form})


class LoginView(View):
    form_class = LoginForm

    def get(self, request):
        form = self.form_class
        return render(request, 'account/login.html' , {'form':form})

    def post(self, request):
        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     cd = form.cleaned_data
        #     account = authenticate(
        #         request, phone_number=cd['phone_number'], password=cd['password'])
        #     if account is not None:
        #         auth_login(request, account)
        #         messages.success(
        #             request, 'Login is successfully !!!', 'success')
        #         return redirect('home:home')
        #     else:
        #         messages.error(
        #             request, "Phone number or password is not correct ?", 'danger')
        #         return redirect('home:home')
        phone_number  = request.POST.get('phone number')
        password = request.POST.get('password')
        if phone_number and password:
            return redirect('home:home')
        return redirect('home:home')

class VerifyCodeView(View):
    form_class = VerfiyCodeForm
    def get(self , request):
        form = self.form_class
        return render(request, 'account/verify_otpcode.html' , {'form':form})
    def post(self , request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number = user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if code_instance.code == cd['code']:
                Account.objects.create_user(
                phone_number=user_session['phone_number'], firstname=user_session['firstname'], lastname=user_session['lastname'], password=user_session['password'])
                code_instance.delete()
                messages.success(request , 'you registered!!!' , 'success')
                return redirect('home:home')
            else:
                messages.error(request , 'your code is wrong' , 'danger')
                return redirect('register:verifycode')
        return redirect('home:home')
class LogOutView(View):
    def get(self, request):
        auth_logout(request)
        messages.info(request, 'logout successfully !!!', 'info')
        return redirect('home:home')


class UpdateAccount(View):
    form_class = ProfileForm
    template_name = 'account/editprofile.html'
    def get(self , request):
        account = Account.objects.get(id=request.user.id)
        form = self.form_class(instance=account)
        return render(request , self.template_name , {'form':form})
    def post(self, request):
        form = self.form_class(request.POST ,files=request.FILES  ,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request , 'This user update', 'success')
            return redirect('home:home')
        return render(request , self.template_name , {'form':form})
class ProfileView(View):
    def get(self , request , user_id):
        user = Account.objects.get(id = user_id)
        order = Order.objects.filter(user = request.user)
        return render(request , 'inc/acoount.html' , {'user':user ,'order':order})

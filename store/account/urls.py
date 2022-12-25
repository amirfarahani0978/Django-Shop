from django.urls import path
from .views import RegisterView ,LogOutView , LoginView , ProfileView ,VerifyCodeView


app_name = 'register'
urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('logout/' , LogOutView.as_view() , name='logout'),
    path('login/' , LoginView.as_view() , name='login'),
    path('profile/<int:user_id>/' , ProfileView.as_view() , name='profile'),
    path('verifycode/' , VerifyCodeView.as_view() , name='verifycode')
]

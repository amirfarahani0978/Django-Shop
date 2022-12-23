from django.urls import path
from .views import RegisterView ,LogOutView , LoginView


app_name = 'register'
urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('logout/' , LogOutView.as_view() , name='logout'),
    path('login/' , LoginView.as_view() , name='login')
]

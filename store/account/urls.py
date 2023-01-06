from django.urls import path , include
from .views import RegisterView ,LogOutView , LoginView , ProfileView , UpdateAccount


app_name = 'register'
urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('logout/' , LogOutView.as_view() , name='logout'),
    path('login/' , LoginView.as_view() , name='login'),
    path('profile/<int:user_id>/' , ProfileView.as_view() , name='profile'),
    path('updateprofile/' , UpdateAccount.as_view() , name='update'),
    path('profile/<int:user_id>/' , ProfileView.as_view() , name='profile'),
    path('api/', include('account.api_urls' , namespace='api'))
]

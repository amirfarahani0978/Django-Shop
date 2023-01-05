from django.urls import path
from .api_views import Register ,ProfileUpdateView ,ProfileView
from rest_framework.authtoken import views as token
app_name= 'api'
urlpatterns = [
    path('register/',Register.as_view() , name='register'),
    path('api-token-auth/' , token.obtain_auth_token),
    path('profile/<int:pk>/' , ProfileView.as_view() , name='profile'), 
    path('profile/update/<int:pk>/' , ProfileUpdateView.as_view() , name='update_profile'), 
]
from django.urls import path
from .api_views import Register ,ProfileUpdateView
from rest_framework.authtoken import views as token
app_name= 'api'
urlpatterns = [
    path('register/',Register.as_view() , name='register'),
    path('api-token-auth/' , token.obtain_auth_token),
    path('profile/update/<int:pk>/' , ProfileUpdateView.as_view() , name='update_question'), 
]
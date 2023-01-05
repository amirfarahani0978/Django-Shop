from django.urls import path
from . import views
from rest_framework.authtoken import views as token
app_name= 'api'
urlpatterns = [
    path('register/', views.Register.as_view() , name='register'),
    path('api-token-auth/' , token.obtain_auth_token),
]
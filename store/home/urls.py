from django.urls import path
from .views import Home ,Contact
app_name = 'home'
urlpatterns =[
    path('' , Home.as_view() , name='home'),
    path('category/<slug:category_slug>/' , Home.as_view() , name='category_filter'),
    path ('contact-us/' , Contact.as_view() , name='contact-us')
]
from django.urls import path
from .views import Home
from .views import ProductDetailView
app_name = 'home'
urlpatterns =[
    path('' , Home.as_view() , name='home'),
    path('<slug:slug>/' , ProductDetailView.as_view() , name='datail')
]
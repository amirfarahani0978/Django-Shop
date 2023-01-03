from django.urls import path
from . import views

app_name = 'order'
url_patterns=[
    path('cart/' , views.CartView.as_view() , name='cart')
]
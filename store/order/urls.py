from django.urls import path
from . import views

app_name = 'order'
urlpatterns=[
    path('cart/' , views.CartView.as_view() , name='cart'),
    path('cart/add/<int:product_id>/' , views.CartAddView.as_view() ,name='addcart'),
    path('order/remove/<int:product_id>/' , views.RemoveCardView.as_view() , name='remove'),
]
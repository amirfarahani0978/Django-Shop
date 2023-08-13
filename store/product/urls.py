from django.urls import path , include
from .views import ProductDetailView ,AddWishListView

app_name='product'
urlpatterns = [
    path('<slug:slug>/', ProductDetailView.as_view(), name='details'),
    path('api/' , include('product.api_urls' , namespace='api_product')),
    path('addwisht/' , AddWishListView.as_view() , name = 'addwishlist'),
]

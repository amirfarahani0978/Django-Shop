from django.urls import path , include
from .views import ProductDetailView

app_name='product'
urlpatterns = [
    path('<slug:slug>/', ProductDetailView.as_view(), name='details'),
    path('api/' , include('product.urls' , namespace='api_product')),
]

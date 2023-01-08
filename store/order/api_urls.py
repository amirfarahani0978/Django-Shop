from django.urls import path

from .api_views import OrderApiView
app_name = 'order_api'

urlpatterns = [
    path('order_api/', OrderApiView.as_view(), name="order_api"),
]
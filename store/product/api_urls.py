from django.urls import path , include
from .api_views import CategoryListView

app_name ='api_product'
urlpatterns=[
    path('view/',CategoryListView.as_view() , name='api_product'),
]
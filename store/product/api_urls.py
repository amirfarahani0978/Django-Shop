from django.urls import path , include
from .api_views import CategoryListView
urlpatterns=[
    path('view/',CategoryListView.as_view() , name='api_product'),
]
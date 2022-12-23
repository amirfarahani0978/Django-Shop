from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Product

# Create your views here.
class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'product/detail.html', {'product': product})

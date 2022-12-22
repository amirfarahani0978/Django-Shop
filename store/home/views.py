from django.shortcuts import render
from django.views import View
from product.models import Product
from django.shortcuts import get_object_or_404


class Home(View):
    def get(self, request):
        product = Product.objects.filter(status_available=True)
        return render(request, 'product/product.html', {'product': product})

    def post(self, request):
        return render(request, 'base.html')


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'product/detail.html', {'product': product})

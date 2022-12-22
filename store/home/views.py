from django.shortcuts import render
from django.views import View
from product.models import Product


class Home(View):
    def get(self, request):
        product = Product.objects.filter(available=True)
        return render(request, 'base.html', {'product': product})

    def post(self, request):
        return render(request, 'base.html')

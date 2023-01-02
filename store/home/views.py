from django.shortcuts import render
from django.views import View
from product.models import Product , Category

class Home(View):
    def get(self, request):
        products = Product.objects.filter(status_available=True)
        category = Category.objects.all()
        return render(request, 'base.html', {'products': products})

    # def post(self, request):
    #     return render(request, 'base.html')



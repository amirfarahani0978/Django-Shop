from django.shortcuts import render
from django.views import View
from product.models import Product , Category
from .forms import ContactForm

class Home(View):
    def get(self, request , category_slug=None):
        products = Product.objects.filter(status_available=True)
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug = category_slug)
            products = products.filter(category = category)
        return render(request, 'base.html', {'products': products , 'categories':categories})

    # def post(self, request):
    #     return render(request, 'base.html')

class Contact(View):
    form_class = ContactForm
    def get(self , request):
        ...
    def post(self , request):
        ...

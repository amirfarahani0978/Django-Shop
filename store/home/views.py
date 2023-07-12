from django.shortcuts import render
from django.views import View
from product.models import Product , Category 
from .models import Baner
from .forms import ContactForm

class Home(View):
    def get(self, request , category_slug=None):
        products = Product.objects.order_by('created')[:4]
        baner = Baner.objects.get(title = 'mobin')
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug = category_slug)
            products = products.filter(category = category)
        return render(request, 'base2.html', {'products': products , 'categories':categories , 'baner':baner})

    # def post(self, request):
    #     return render(request, 'base.html')

class Contact(View):
    form_class = ContactForm
    template_name = 'contact-us.html'
    def get(self , request):
        ...
    def post(self , request):
        ...

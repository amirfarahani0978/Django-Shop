from django.shortcuts import render
from django.views import View
from product.models import Product , Category 
from .models import Baner
from .forms import ContactForm

class Home(View):
    def get(self, request , category_slug=None):
        products = Product.objects.order_by('created')[:4]
        baner = Baner.objects.get(title = 'mobin')
        return render(request, 'home_page.html', {'products': products , 'baner':baner })

    # def post(self, request):
    #     return render(request, 'base.html')

class Contact(View):
    form_class = ContactForm
    template_name = 'inc/contact-us.html'
    def get(self , request):
        return render(request, self.template_name)
    def post(self , request):
        ...

class AboutUsView(View):
    template_name = 'inc/about_us.html'
    def get(self , request):
        return render(request , self.template_name)
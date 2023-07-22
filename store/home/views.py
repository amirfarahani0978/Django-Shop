from django.shortcuts import render
from django.views import View
from product.models import Product , Category 
from .models import Baner
from .forms import ContactForm

class Home(View):
    def get(self, request , category_slug=None):
        products = Product.objects.order_by('created')[:4]
        baner = Baner.objects.get(title = 'mobin')
        category_header = Category.objects.all()
        return render(request, 'home_page.html', {'products': products , 'baner':baner , 'categories' : category_header})

    # def post(self, request):
    #     return render(request, 'base.html')

class Contact(View):
    form_class = ContactForm
    template_name = 'contact-us.html'
    def get(self , request):
        return render(request, self.template_name)
    def post(self , request):
        ...

class AboutUsView(View):
    def get(self , request):
        return render(self , 'store/about_us.html')
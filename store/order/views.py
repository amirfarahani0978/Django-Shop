from django.shortcuts import render,get_object_or_404, redirect
from django.views import View
from .cart import Cart
from product.models import Product
from .forms import CartAddForm
class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/cart.html' , {'cart':cart})


class CartAddView(View):
    def post(self, request , product_id):
        cart = Cart(request)
        product = get_object_or_404(Product , id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product , form.cleaned_data['quantity'])
        return redirect('order:cart')


class RemoveCardView(View):
    def get(self, request , product_id):
        cart = Cart(request)
        product = get_object_or_404(Product ,id = product_id)
        cart.remove(product)
        return redirect('order:cart')
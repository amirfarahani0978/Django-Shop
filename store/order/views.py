from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from product.models import Product
from .forms import CartAddForm, OfferForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from account.models import Account


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('order:cart')


class RemoveCardView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('order:cart')


class DetailOrderView(LoginRequiredMixin, View):
    form_class = OfferForm

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'order/order.html', {'order': order, 'form': self.form_class})


class CreateOrderView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(
                order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        cart.clear()
        return redirect('order:detail_order', order.id)


class CheckProfileCart(LoginRequiredMixin, View):
    def get(self, request):
        user = Account.objects.get(id=request.user.id)
        if request.user.postal_code is not None:
            return render(request, 'order/checkprofile.html', {'user': user})
        return render(request, 'order/error.html')

class OfferApplyView(LoginRequiredMixin , View):
    pass
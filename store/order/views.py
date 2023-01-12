from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from product.models import Product
from .forms import CartAddForm, OfferForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem, Offer
from account.models import Account
import datetime
from django.contrib import messages
from product.models import Product


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
        for item in cart:
            quant_store = Product.objects.get(slug=item['product'])
            if item['quantity'] > quant_store.quantity:
                messages.error(
                    request, f"Sorry, this {item['product']}is not available in the quantity you requested", 'danger')
                return redirect('order:cart')
        order = Order.objects.create(user=request.user)
        for item in cart:
            quant_store = Product.objects.get(slug=item['product'])
            OrderItem.objects.create(
                order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            quant_store.quantity -= item['quantity']
            quant_store.save()

        cart.clear()
        return redirect('order:detail_order', order.id)


class CheckProfileCart(LoginRequiredMixin, View):
    def get(self, request):
        user = Account.objects.get(id=request.user.id)
        if request.user.postal_code is not None:
            return render(request, 'order/checkprofile.html', {'user': user})
        return render(request, 'order/error.html')


class OfferApplyView(LoginRequiredMixin, View):
    form_class = OfferForm

    def post(self, request, order_id):
        now = datetime.datetime.now()
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                offer = Offer.objects.get(
                    offer_code__exact=code, start_time__lte=now, expire_time__gte=now, is_available=True)
            except Offer.DoesNotExist:
                messages.error(
                    request, "This coupon does'nt exist!!!", 'danger')
                return redirect('order:detail_order', order_id)
            order = Order.objects.get(id=order_id)
            order.offer = offer.percent
            order.save()
            return redirect('order:detail_order', order_id)

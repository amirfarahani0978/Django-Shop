from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from product.models import Product
from .forms import CartAddForm, OfferForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem, Offer 
from account.models import Account
import datetime
from django.contrib import messages
from product.models import Product
from django.conf import settings
import requests
import json
from django.http import JsonResponse
from .cart import Cart
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt



class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/cart.html', {'cart': cart})
    # def get(self , request):
    #     cart = None
    #     cartitems = []
        
    #     if request.user.is_authenticated:
    #         cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    #         cartitems = cart.cartitems.all()
        
    #     context = {"cart":cart, "items":cartitems}
    #     return render(request, 'order/cart.html', context)

class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('order:cart')
    # def post(self , request):
    #     data = json.loads(request.body)
    #     product_id = data['id']
    #     product = get_object_or_404(Product, id=product_id)
    #     if request.user.is_authenticated:
    #         cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    #         cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
    #         cartitem.quantity += 1
    #         cartitem.save()
    #     return JsonResponse('it is ok', safe=False)


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


if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
CallbackURL = 'http://127.0.0.1:8080/verify/'


class OrderPayView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": order.get_total_price(),
            "Description": description,
            "Phone": requests.user.phone_number,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json',
                   'content-length': str(len(data))}
        try:
            response = requests.post(
                ZP_API_REQUEST, data=data, headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
                else:
                    return {'status': False, 'code': str(response['Status'])}
            return response

        except requests.exceptions.Timeout:
            return {'status': False, 'code': 'timeout'}
        except requests.exceptions.ConnectionError:
            return {'status': False, 'code': 'connection error'}

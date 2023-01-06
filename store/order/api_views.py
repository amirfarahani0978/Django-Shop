from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import json

import requests

from account.models import Account
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemsSerializer, ItemSerializer
from product.models import Product, Category


class OrderApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order_ser = OrderSerializer(instance=Order.objects.all(), many=True)
        order_items_ser = OrderItemsSerializer(
            instance=OrderItem.objects.all(), many=True)
        content = {
            "orders": order_ser.data,
            "order_item": order_items_ser.data,
            "user": request.user.id
        }
        return Response(content)

    def post(self, request):
        user = request.user
        account = Account.objects.get(user=user)
        if account.default_address is not None:
            order = Order.objects.create(
                costumer=account, address_id=account.default_address.id)
            check = ItemSerializer(data=request.data, many=True)
            if check.is_valid():
                for i in request.data:
                    i["order"] = order.id
                    item = Product.objects.get(
                        name=i["name"].replace("_", " "))
                    i["item"] = item.id
                    i["quantity"] = i["count"]
                    del i["name"]
                    del i["price"]
                    del i["count"]
                    order_f = OrderItemsSerializer(data=i)
                    if order_f.is_valid():
                        order_f.save()
                    else:
                        raise ProcessLookupError
                order.save()
                resp = requests.post("https://api.idpay.ir/v1.1/payment",
                                     headers={'Content-Type': 'application/json',
                                              "X-API-KEY": 'c377d98e-0c65-4696-9d7f-db122b15b5e0',
                                              'X-SANDBOX': "1"},
                                     data=json.dumps({"order_id": order.id, "amount": int(order.get_total_cost) * 28000,
                                                      "name": f"{costumer.user.phone}",
                                                      "phone": f"{costumer.user.phone}",
                                                      "mail": f"{costumer.user.email}",
                                                      "desc": f"From Costumer : {costumer.id}",
                                                      "callback": "http://185.235.41.190:8000/"})
                                     ).json()
                if "link" in resp.keys():
                    Transactions.objects.create(
                        order=order, transactionId=resp["id"], transactionLink=resp["link"])
                    order.status = 3
                    order.save()
                    send_mail(
                        'Congratulations !',
                        f'Dear Admin , You Received A New Order From Customer : {costumer.user.username} ! With Transaction Id : {resp["id"]}',
                        from_email=None,
                        recipient_list=["mobinatashi2@gmail.com"],
                        fail_silently=False,
                    )
                    return Response(resp["link"])
                else:
                    order.status = 0
                    order.save()
                    return Response({"Error": "Transaction Failed !"}, status=401)
        else:
            return Response({"Error": "At First Please Login/Select A valid Default Address :)"}, status=401)

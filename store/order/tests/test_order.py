from django.test import TestCase
from order.models import Order, OrderItem


class TestOrder(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            state="Ordering",
            time="12/9/2022 1:23:21",
            total_price=200
        )

    def test_order_creation(self):
        self.assertEqual(self.order.state, "Ordering")
        self.assertEqual(self.order.time, "12/9/2022 1:23:21")
        self.assertEqual(self.order.total_price, 200)

    def test_order_str(self):
        self.assertEqual(str(self.order), f"{self.time} {self.total_price}")


class TestOrderItem(TestCase):
    def setUp(self):
        self.order_item = OrderItem.objects.create(
            quantity=200,
        )

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.quantity, 200)

    def test_order_item_str(self):
        self.assertEqual(str(self.order_item), self.quantity)

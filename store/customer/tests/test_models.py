from django.test import TestCase
from customer.models import Customer , Address


class TestCustomer(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            firstname = "amirhossien",
            lastname = "hassani",
            birth_date = "2022-12-09 10:38:52",
            postal_code = 1774963941
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.firstname , "amirhossien")
        self.assertEqual(self.customer.lastname , "hassani")
        self.assertEqual(self.customer.birth_date , "2022-12-09 10:38:52")
        self.assertEqual(self.customer.postal_code , 1774963941)
    
    def test_user_str(self):
        self.assertEqual(str(self.customer),self.firstname)
class TestAddress(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            address = "Azadi street"
        )
    
    def test_address_creation(self):
        self.assertEqual(self.address.address , "Azadi street")

    def test_address_str(self):
        self.assertEqual(str(self.address),self.address)
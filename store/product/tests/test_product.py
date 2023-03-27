from django.test import TestCase
from product.models import Category, ProductFeature , Product , Offer , Comment


class TestCategory(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Date'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Date')

    def test_category_str(self):
        self.assertEqual(str(self.category), self.name)


class TestProductFeature(TestCase):
    def setUp(self):
        self.prodcutfeature = ProductFeature.objects.create(
            amount=199 ,
            descript='litr'
        )

    def test_productfeature_creation(self):
        self.assertEqual(self.prodcutfeature.amount, 199)
        self.assertEqual(self.prodcutfeature.descript, 'lire')

    def test_productfeature_str(self):
        self.assertEqual(str(self.prodcutfeature), self.amount)

class TestProduct(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(
            name = 'date', 
            price = 200,
            count_buying = 2, 
            status_available = True, 
            quantity = 4,
            rate = 10 
        )
    def test_product_creation(self):
        self.assertEqual(self.product.name, 'date')
        self.assertEqual(self.product.price, 200)
        self.assertEqual(self.product.count_buying, 2)
        self.assertEqual(self.product.status_available,True)
        self.assertEqual(self.product.quantity,4)
        self.assertEqual(self.product.rate, 10)
        

    def test_product_str(self):
        self.assertEqual(str(self.product), f"{self.name} {self.price} {self.status_available}")

class TestOffer(TestCase):
    def setUp(self) -> None:
        self.offer = Offer.objects.create(
            expire_time = '12/9/2022 2:3:12' ,
            start_time = '12/9/2022 1:3:12',
            min_price = 200,
            max_price = 400, 
            percent = 40, 
            is_available  = False,
        )
    def test_offer_creation(self):
        self.assertEqual(self.offer.expire_time, '12/9/2022 2:3:12')
        self.assertEqual(self.offer.start_time, '12/9/2022 1:3:12')
        self.assertEqual(self.offer.min_price, 200)
        self.assertEqual(self.offer.max_price, 400)
        self.assertEqual(self.offer.percent,40)
        self.assertEqual(self.offer.is_available,False)
        

class TestComment(TestCase):
    def setUp(self) -> None:
        self.comment = Comment.objects.create(
            cooment = 'this is good product',
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.comment ,'this is good product')

    def test_comment_str(self):
        self.assertEqual(str(self.comment) , f"{self.profile_id} {self.product_id}")
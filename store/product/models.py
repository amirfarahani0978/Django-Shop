from django.db import models
from account.models import Account
from core.models import BaseModel
from django.urls import reverse


class Category(BaseModel):
    sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='subcategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Catagories'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_filter', args=[self.slug,])


class ProductFeature(BaseModel):
    amount = models.PositiveIntegerField()
    descript = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return f'{self.amount}'


class Product(BaseModel):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    price = models.PositiveIntegerField()
    count_buying = models.PositiveIntegerField()
    status_available = models.BooleanField()
    quantity = models.PositiveIntegerField()
    category = models.ManyToManyField(
        Category, related_name='products')
    rate = models.PositiveIntegerField(default=50)
    created = models.DateTimeField(auto_now=True)
    product_feature = models.OneToOneField(
        ProductFeature, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('product:details', args=[self.slug,])
    
    def get_star_representation(self):
        full_stars = '<i class="fas fa-star"></i>' * (self.rate // 20)
        half_star = '<i class="fas fa-star-half-alt"></i>' if (self.rate % 20 >= 10) else ''
        empty_stars = '<i class="far fa-star"></i>' * (5 - (self.rate // 20) - (1 if half_star else 0))

        return f"{full_stars}{half_star}{empty_stars}"
    
    def comment_count(self):
        return self.comments.count()


class Comment(BaseModel):
    profile_id = models.OneToOneField(Account, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='comments')
    created_time = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.comment

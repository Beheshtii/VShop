from django.db import models
from accounts.models import User
from decimal import Decimal

class ProductStatusType(models.IntegerChoices):
    active = 1, ('فعال')
    inactive = 2, ('غیر فعال')

class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.title

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='products')
    category = models.ManyToManyField('ProductCategory')
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(upload_to='products/images/')
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices, default=ProductStatusType.active)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    discount_percent = models.PositiveSmallIntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_raw_price(self):
        return int(self.price)

    def get_real_price(self):
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return int(discounted_amount)

    class Meta:
        db_table = 'product'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='extra_images')
    image = models.ImageField(upload_to='products/extra-images/')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_image'




from django.db import models

from applications.account.models import Profile
from applications.category.models import Category


class Goods(models.Model):

    title = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='profile')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='goods')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class GoodsImage(models.Model):
    product = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='products_photo')

    def __str__(self):
        return self.product.title

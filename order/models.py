from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


from product.models import *
# Create your models here.
class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return self.product.price  
    
    @property
    def amount(self):
        return (self.product.price * self.quantity)

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
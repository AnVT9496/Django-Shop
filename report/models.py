from django.db import models
from order.models import Order, OrderDetail
from product.models import Product

# Create your models here.

class SalesReport(Order):
    class Meta:
        proxy = True


class ProductReport(OrderDetail):
    class Meta:
        proxy = True


from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

# Register your models here.
from order.models import *


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user']

class OrderDetailline(admin.TabularInline):
    model = OrderDetail
    readonly_fields = ('user', 'product','price','quantity','amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name','phone','city','total','status']
    list_filter = ['status',]
    readonly_fields = ('user','address','city','country','phone','first_name','ip', 'last_name','phone','city','total','voucher', 'total_after_used_voucher','create_at')
    can_delete = False
    inlines = [OrderDetailline]

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','price','quantity','amount']
    list_filter = ['user']

    
admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)

from product.models import Category
from django.contrib import admin
from product.models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent', 'status']
    list_filter = ['status']

# add thêm 3 fields image vào Product trong Admin
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status','image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]



admin.site.register(Category, CategoryAdmin)   
admin.site.register(Product, ProductAdmin) 
admin.site.register(Images) 
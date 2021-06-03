from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),    
    )
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to = 'images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),    
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to = 'images/', null= False)
    price = models.FloatField()
    amount = models.IntegerField()
    min_amount = models.IntegerField()
    detail = RichTextUploadingField()
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Image tag ảnh trong admin
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
        ## method to create a fake table field in read only mode
    # def image_tag(self):
    #         return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        
    # image_tag.short_description = 'Image'

    #  ảnh phụ của product
class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to = 'images/')

    def __str__(self):
        return self.title

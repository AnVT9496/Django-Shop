from django.contrib import admin

# Register your models here.
from user.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','image_tag']

    def has_add_permission(self, request):
        return False
admin.site.register(UserProfile,UserProfileAdmin)


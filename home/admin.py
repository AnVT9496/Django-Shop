from home.models import Setting
from django.contrib import admin
from home.models  import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']

#check message được gửi từ contact trong admin
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']

    def has_add_permission(self, request):
        return False
        
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

class UserAdmin(BaseUserAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Session, SessionAdmin)


admin.site.register(Setting, SettingsAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
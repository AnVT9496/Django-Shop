from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from rangefilter.filters import DateRangeFilter
from django.db.models import Count, Sum
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


@admin.register(SalesReport)
class ReportAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    list_filter = ['status', 'user', ('create_at', DateRangeFilter),]
    # date_hierarchy = 'create_at'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Sum('total'),
            'total_after_used_voucher': Sum('total_after_used_voucher'),
        }

        response.context_data['summary'] = list(
            qs
            .values('first_name', 'status', 'create_at')
            .annotate(**metrics)
        )

        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        return response

    
admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)

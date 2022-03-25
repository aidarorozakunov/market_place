from django.contrib import admin

from applications.order.models import Order, OrderGoods


class OrderGoodsInline(admin.TabularInline):
    model = OrderGoods
    extra = 1
    fields = ('goods', 'quantity', 'total_cost')


class OrderAdminDisplay(admin.ModelAdmin):
    inlines = [OrderGoodsInline, ]
    list_display = ('user', 'status')
    list_editable = ('status', )


admin.site.register(Order, OrderAdminDisplay)

from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.goods.models import GoodsImage, Goods


class InlineGoodsImage(admin.TabularInline):
    model = GoodsImage
    extra = 1
    fields = ['image', ]


class GoodsAdminDisplay(admin.ModelAdmin):
    inlines = [InlineGoodsImage, ]
    list_display = ('title', 'in_stock', 'quantity', 'image', 'get_first_name', 'get_phone_number')
    list_editable = ('in_stock', 'quantity')
    search_fields = ('title', )
    list_filter = ('category', )

    @admin.display(ordering='profile__first_name', description='first_name')
    def get_first_name(self, obj):
        return obj.profile.first_name

    @admin.display(ordering='profile__number', description='phone_number')
    def get_phone_number(self, obj):
        return obj.profile.number

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain" />')
        else:
            return ""


admin.site.register(Goods, GoodsAdminDisplay)




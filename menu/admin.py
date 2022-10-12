from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Gallery


class GalleryInlineAdmin(admin.TabularInline):
    model = Gallery
    min_num = 1
    readonly_fields = ['show_image']

    def show_image(self, obj):
        return mark_safe(f"<a href='{obj.image.url}' ><img src='{obj.image.url}' width={150} height={200}></a>")

    show_image.short_description = 'Images'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'create_at', 'update_at', 'get_products_count', 'show_category_image')

    def show_category_image(self, instance):
        if instance is None:
            return ""
        url = instance.image.url
        return mark_safe(f'<a href="{url}"> <img src="{url}" width="{150}" height={100} /></a>')

    show_category_image.short_description = 'Image'

    def get_products_count(self, instance):
        if instance is None:
            return "-"
        return instance.products.available().count()

    get_products_count.short_description = 'Products'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'featured', 'active', 'create_at', 'update_at', 'show_product_image')
    inlines = [GalleryInlineAdmin, ]
    readonly_fields = ('show_product_image', )

    def show_product_image(self, instance):
        if instance is None:
            return ""
        url = instance.image.url
        return mark_safe(f'<a href="{url}"> <img src="{url}" width="{150}" height={100} /></a>')

    show_product_image.short_description = 'Image'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

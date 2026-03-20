from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock", "created_at", "edit_button")
    search_fields = ("name", "description")
    list_filter = ("created_at",)
    list_display_links = ("id", "name")
    inlines = [ProductImageInline]

    def edit_button(self, obj):
        url = reverse('admin:products_product_change', args=[obj.id])
        return format_html('<a class="button" style="padding: 4px 10px; background-color: #417690; color: white; border-radius: 4px; text-decoration: none; font-weight: bold;" href="{}">Edit</a>', url)
    edit_button.short_description = "Action"
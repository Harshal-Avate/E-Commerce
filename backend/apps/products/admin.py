from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Category, Product, ProductImage



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "stock", "created_at", "edit_button")
    search_fields = ("name", "description")
    list_filter = ("category", "created_at")
    list_display_links = ("id", "name")
    inlines = [ProductImageInline]

    def edit_button(self, obj):
        url = reverse('admin:products_product_change', args=[obj.id])
        return format_html('<a class="button" style="padding: 4px 10px; background-color: #417690; color: white; border-radius: 4px; text-decoration: none; font-weight: bold;" href="{}">Edit</a>', url)
    edit_button.short_description = "Action"
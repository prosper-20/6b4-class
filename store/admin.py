from django.contrib import admin
from .models import Product, Category



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "is_available"]
    list_filter = ["is_available", "category"]
    list_editable = ["price"]
    prepopulated_fields = {"slug": ("name",)}


# admin.site.register(Product, ProductAdmin)

admin.site.register(Category)
from django.contrib import admin
from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name']

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'category', 'price', 'quantity', 'discount']
    list_editable = ['discount']
    search_fields = ['name', 'description']
    list_filter = ['category', 'quantity', 'discount']
    fields = [
        'slug',
        'name',
        'category',
        'description',
        'image',
        ('price', 'discount'),
        'quantity',
    ]
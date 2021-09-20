from django.contrib import admin
from .models import Category,Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'ordering')
    list_filter = ('slug',)
    search_fields = ('slug',)
    ordering = ('ordering',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category','vendor')
    list_filter = ('slug',)
    search_fields = ('slug',)
    ordering = ('category','price','date_added')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
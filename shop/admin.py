from django.contrib import admin
from django.db import models
from .models import Product, Order
# Register your models here.

admin.site.site_header = "My E-Commerce WebSite"
admin.site.site_title = "My Shopping"
admin.site.index_title = "Manage Shopping"

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price', 'category']
    search_fields = ('title','category')
    list_editable = ('price','category')
    



admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
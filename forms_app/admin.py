from django.contrib import admin
from .models import Product

# Register your models here.
# admin interface is a model-centric interface (allows performing CRUD operations on models through GUI)


#  customizing django admin interface
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    ordering = ('-price',)


admin.site.register(Product, ProductAdmin)

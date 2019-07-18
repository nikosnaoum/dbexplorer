from django.contrib import admin

from .models import Product, Category, FuelType, GearBox, Brand, RepairedDamage


admin.site.register(Category)

admin.site.register(FuelType)

admin.site.register(GearBox)

admin.site.register(Brand)

admin.site.register(RepairedDamage)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Product, ProductAdmin)


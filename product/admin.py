from django.contrib import admin

from .models import Product, Cart, Order, PayStripe

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)

admin.site.register(PayStripe)
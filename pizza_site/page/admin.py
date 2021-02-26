from django.contrib import admin
from .models import Pizza, Category, Menu, Order, OrderItem, Customer, ShippingAddress

admin.site.register(Customer)
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)
admin.site.register(Menu)



from django.contrib import admin
from core.models import Restaurant, Sale, Rating, Product, Order, Account, Transfer

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Sale)
admin.site.register(Rating)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Account)
admin.site.register(Transfer)

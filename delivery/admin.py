from django.contrib import admin

from .models import Delivery, Address, Type


admin.site.register(Delivery)
admin.site.register(Address)
admin.site.register(Type)

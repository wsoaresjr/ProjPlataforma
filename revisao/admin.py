# revisao/admin.py

from django.contrib import admin
from .models import Item, ItemRevisor

admin.site.register(Item)
admin.site.register(ItemRevisor)

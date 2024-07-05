from django.contrib import admin
from menu.models import Coffees

# Register your models here.

@admin.register(Coffees)
class CoffeesAdmin(admin.ModelAdmin):
    pass


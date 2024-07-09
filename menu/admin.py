from django.contrib import admin
from menu.models import Coffees
from menu.models import Publication

# Register your models here.

@admin.register(Coffees)
class CoffeesAdmin(admin.ModelAdmin):
    pass



@admin.register(Publication)
class BlogAdmin(admin.ModelAdmin):
    pass


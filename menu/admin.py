from django.contrib import admin
from menu.models import Coffees, Feedback, MokkoContact, ClientContact, NameVerbose
from menu.models import Publication

# Register your models here.

@admin.register(Coffees)
class CoffeesAdmin(admin.ModelAdmin):
    pass



@admin.register(Publication)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['full_name']


@admin.register(MokkoContact)
class MokkoContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')


@admin.register(ClientContact)
class ClientContactAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(NameVerbose)
class NameVerbose(admin.ModelAdmin):
    pass

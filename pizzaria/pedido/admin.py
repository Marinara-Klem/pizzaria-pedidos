from django.contrib import admin
from pedido.models import Pedido, Item

# Register your models here.

class ItemTabularAdmin(admin.TabularInline):
    list_display = ['quantidade', 'pedido', 'pizza']
    extra = 1

    model = Item


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente']

    inlines = [ItemTabularAdmin]

admin.site.register(Pedido, PedidoAdmin)
# admin.site.register(Item, ItemTabularAdmin)
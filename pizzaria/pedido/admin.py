from django.contrib import admin
from pedido.models import Pedido, Item

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['quantidade', 'pedido', 'pizza']

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Item, ItemAdmin)
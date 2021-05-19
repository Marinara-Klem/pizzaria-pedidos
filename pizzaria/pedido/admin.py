from django.contrib import admin
from django import forms
from pedido.models import Pedido, Item, Endereco
from pizza.models import Pizza

# Register your models here.
class ItemTabularAdmin(admin.TabularInline):
    list_display = ['quantidade', 'pizza']
    extra = 1
    model = Item

class EnderecoStackedAdmin(admin.StackedInline):
    list_display = ['bairro']
    extra = 1
    max_num = 1
    model = Endereco

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_do_pedido']
    readonly_fields = ['data_do_pedido']
    list_filter = ['data_do_pedido']

    ordering = ['-data_do_pedido']

    inlines = [ItemTabularAdmin, EnderecoStackedAdmin]


admin.site.register(Pedido, PedidoAdmin)
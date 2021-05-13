from django.contrib import admin
from django import forms
from pedido.models import Pedido, Item
from pizza.models import Pizza

# Register your models here.

# class PizzaCardapioForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.fields['pizza'].queryset = Pizza.objects.filter(ativo=True)


class ItemTabularAdmin(admin.TabularInline):
    list_display = ['quantidade', 'pizza']
    extra = 1

    # class ItemForm(PizzaCardapioForm):
    #     pass

    # form = ItemForm
    

    model = Item


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_do_pedido']
    readonly_fields = ['data_do_pedido']
    list_filter = ['data_do_pedido']

    ordering = ['-data_do_pedido']

    inlines = [ItemTabularAdmin]

admin.site.register(Pedido, PedidoAdmin)
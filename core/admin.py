from django.contrib import admin

# Register your models here.
from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('tipo_categoria', 'precoMaximo')

admin.site.register(Pedido, PedidoAdmin)
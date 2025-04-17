from django.contrib import admin
from django.contrib import messages
from django.db import models
from .models import Categoria, Producto, Cliente


# Configuración global del admin
admin.site.site_header = "Mi Super Admin"

# Registro de modelos (USANDO SOLO UN MÉTODO POR MODELO)

# Opción 1: Usando decorador @admin.register (recomendado)
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    
    def __str__(self):
        return self.nombre

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    actions = ['incrementar_stock']

    def incrementar_stock(self, request, queryset):
        cantidad = 20
        actualizados = queryset.update(stock=models.F('stock') + cantidad)
        self.message_user(
            request,
            f'Stock incrementado en {cantidad} unidades para {actualizados} productos',
            messages.SUCCESS
        )
    incrementar_stock.short_description = "Incrementar stock en 20 unidades"

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'telefono', 'email')
    search_fields = ('nombres', 'apellidos', 'dni')
    list_filter = ('fecha_publicacion',)
    ordering = ('apellidos', 'nombres')
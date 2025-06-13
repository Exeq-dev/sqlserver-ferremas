from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username','run', 'pnombre', 'snombre', 'ap_paterno', 'ap_materno', 'fecha_nacimiento', 'direccion']
    search_fields = ['run']
    list_per_page = 10
    list_filter = ['ap_paterno']
    list_editable = ['pnombre', 'run', 'snombre', 'ap_paterno', 'ap_materno', 'fecha_nacimiento', 'direccion']

admin.site.register(usuarioCustom, UsuarioAdmin)
admin.site.register(rolUsuario)
admin.site.register(comuna)
admin.site.register(region)
admin.site.register(producto)
admin.site.register(marca)
admin.site.register(categoriaProducto)

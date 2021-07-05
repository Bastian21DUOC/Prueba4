from django.contrib import admin

from .models import Sucursal, Producto, Usuario

admin.site.register(Sucursal)
admin.site.register(Producto)
admin.site.register(Usuario)

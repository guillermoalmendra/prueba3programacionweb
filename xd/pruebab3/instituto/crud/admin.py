from django.contrib import admin
from .models import Producto, Tipoproducto, Marca, FormaPago, Venta, nivelEstudio, Region, tipoUsuario, Cliente, Afiliado #hay que declarar todos los modelos 
# Register your models here.

admin.site.register(Producto)
admin.site.register(Tipoproducto)#listo
admin.site.register(Marca) #listo
admin.site.register(FormaPago)#listo
admin.site.register(Venta)
admin.site.register(Region)#listo
admin.site.register(tipoUsuario)#listo
admin.site.register(nivelEstudio)#listo
admin.site.register(Cliente)
admin.site.register(Afiliado)#listo
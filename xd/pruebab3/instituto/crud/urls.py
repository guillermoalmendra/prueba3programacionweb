from .import views
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('marca',views.marca,name='marca'),
    path('tipoproducto',views.tipoproducto,name='tipoproducto'),
    path('formapago',views.formapago,name='formapago'),
    path('nivelestudio',views.nivelestudio,name='nivelestudio'),
    path('region',views.region,name='region'),
    path('tipousuario',views.tipousuario,name='tipousuario'),
    path('afiliado',views.afiliado,name='afiliado'),
    path('clienteForm',views.clienteForm,name='clienteForm'),
    path('ventaForm',views.ventaForm,name='ventaForm'),
    path('productoForm',views.productoForm,name='productoForm'),
    path('menu', views.menu, name='menu'),
    

]

# 127.0.0.1:8000/crud/marca
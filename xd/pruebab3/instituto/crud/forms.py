from django import forms
from django.forms import ModelForm

from .models import Cliente, Venta, Producto

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields= "__all__"


class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields= "__all__"


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields= "__all__"

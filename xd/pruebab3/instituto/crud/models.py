from django.db import models
####creación de un producto
class Tipoproducto(models.Model):
    idtTipoproducto= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    idMarca= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()


    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    idProducto=models.AutoField(primary_key=True)
    nombreProducto= models.CharField(max_length=50, null=False, unique=True,blank=False)
    descripcion= models.CharField(max_length=500, null=False, unique=True,blank=False)
    peso= models.CharField(max_length=50, null=False, unique=True,blank=False)
    precio = models.CharField(max_length=999999, default='')
    stock = models.CharField(max_length=1000, default='')
    Tipoproducto = models.ForeignKey(Tipoproducto, db_column='idtTipoproducto',
                               on_delete=models.CASCADE,
                               null=True, blank=True)
    Marca = models.ForeignKey(Marca, db_column='idMarca',
                               on_delete=models.CASCADE,
                               null=True, blank=True)
    activo= models.BooleanField()
    
    def __str__(self):
        return self.nombreProducto

################################## venta
class FormaPago(models.Model):
    idTipoPago= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()
    
    def __str__(self):
        return self.nombre


class Venta(models.Model):
    idVenta=models.AutoField(primary_key=True)
    nombreVenta = models.CharField(max_length=50, null=True, unique=True)
    precio = models.CharField(max_length=999999, default='')
    tipoPago = models.ForeignKey(FormaPago, db_column='idTipoPago',
                               on_delete=models.CASCADE,
                               null=True, blank=True)
    idProducto = models.ForeignKey(Producto, db_column='idProducto',
                               on_delete=models.CASCADE,
                               null=True, blank=True)
    
    def __str__(self):
        return self.nombreVenta
    
class nivelEstudio(models.Model):
    idNivel= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

    
class Region(models.Model):
    idRegion= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class tipoUsuario(models.Model):
    idTipoUsuario= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class Afiliado(models.Model):
    idAfiliado= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    idCliente= models.AutoField(primary_key=True)
    rut = models.IntegerField(unique=True, null=False, blank=False)
    dv = models.CharField(max_length=1,null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, unique=False)
    direccion = models.CharField(max_length=50, null=False, unique=False)
    apellido = models.CharField(max_length=50, null=False, unique=False)
    telefono = models.CharField(max_length=50, null=False, unique=False)
    email = models.EmailField(max_length=50, null=False, unique=False)
    tipoUsuario = models.ForeignKey(tipoUsuario, db_column='idTipoUsuario',
                               on_delete=models.CASCADE,
                               null=True, blank=True)
    region = models.ForeignKey(Region, db_column='idRegion',
                               on_delete=models.CASCADE,
                               null=True, blank=True)
    nivelDeEstudio = models.ForeignKey(nivelEstudio, db_column='idNivel',
                               on_delete=models.CASCADE,
                               null=True, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido



# PASOS:
# 1.- para preparar la migración:
# py manage.py makemigrations crud
# 2.- hacer migracion
# py manage.py migrate crud
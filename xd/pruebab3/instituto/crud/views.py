from django.shortcuts import render
from .models import Marca, Tipoproducto, FormaPago, nivelEstudio, Region, tipoUsuario, Afiliado
# Create your views here.
from .forms import ClienteForm, VentaForm, ProductoForm
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    return render(request, 'menu.html')

def clienteForm(request):
    context = {'form':  ClienteForm()}
    if request.method == 'POST':
        if 'Grabar' in request.POST:
            form = ClienteForm(request.POST)

            if form.is_valid():
                form.save()
                context['exito']='Datos guardados'
            else:                
                context['error']='Datos No guardados'

    return render(request, 'clienteForm.html', context)
@login_required
def ventaForm(request):
    context = {'form':  VentaForm()}
    if request.method == 'POST':
        if 'Grabar' in request.POST:
            form = VentaForm(request.POST)

            if form.is_valid():
                form.save()
                context['exito']='Datos guardados'
            else:                
                context['error']='Datos No guardados'

    return render(request, 'VentaForm.html', context)
@login_required
def productoForm(request):
    context = {'form':  ProductoForm()}
    if request.method == 'POST':
        if 'Grabar' in request.POST:
            form = ProductoForm(request.POST)

            if form.is_valid():
                form.save()
                context['exito']='Datos guardados'
            else:                
                context['error']='Datos No guardados'

    return render(request, 'ProductoForm.html', context)
@login_required
def marca(request): 

    #orm
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                Marca.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = Marca.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = Marca.objects.all() # select * from marca
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Marca.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Marca.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'marca.html', context)
@login_required
def tipoproducto(request): 

    #orm
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                Tipoproducto.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = Tipoproducto.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = Tipoproducto.objects.all() 
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Tipoproducto.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Tipoproducto.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'tipoproducto.html', context)

@login_required
def formapago(request): 
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                FormaPago.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = FormaPago.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = FormaPago.objects.all() 
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = FormaPago.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = FormaPago.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'formapago.html', context)
@login_required
def nivelestudio(request): 
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                nivelEstudio.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = nivelEstudio.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = nivelEstudio.objects.all() 
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = nivelEstudio.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = nivelEstudio.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'nivelestudio.html', context)

@login_required
def region(request): 
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                Region.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = Region.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = Region.objects.all() 
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Region.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Region.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'region.html', context)
@login_required
def tipousuario(request): 
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                tipoUsuario.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = tipoUsuario.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = tipoUsuario.objects.all() 
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = tipoUsuario.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = tipoUsuario.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'tipousuario.html', context)

@login_required
def afiliado(request): 
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                Afiliado.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = Afiliado.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = Afiliado.objects.all() 
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Afiliado.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Afiliado.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'afiliado.html', context)
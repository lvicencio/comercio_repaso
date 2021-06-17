from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import login,authenticate
# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado con Exito"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')


def agregar_producto(request):
    data={
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Registrado con Exito")
        else:
            data["form"] = formulario

    
    return render(request, 'app/producto/nuevo.html', data)


def listar_productos (request):
    productos = Producto.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 2)
        productos = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listar.html', data)


def editar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)

    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado de manera correcta!!")
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario

    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto Eliminado Correctamente!!")
    return redirect(to="listar_producto")


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado con Exito")
            return redirect(to="home")
        data["form"] = formulario



    return render(request, 'registration/registrar.html', data)
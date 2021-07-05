from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Sucursal
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'cakehouse/index.html')


def Ver_productos(request):
    listado_productos = Producto.objects.all()
    context = {'listado_productos': listado_productos}
    return render(request, 'cakehouse/Ver_productos.html', context)

def Inicio_sesion(request):
    return render(request, 'cakehouse/Inicio_sesion.html')

def F_Inicio_sesion(request):
    rut = request.POST["rut"]
    clave = request.POST["clave"]

    user = authenticate(username=rut, password=clave)

    if user is not None:        
        login(request,user)
        rut = user.rut        
        context = {'rut': rut}
        return render(request, 'cakehouse/index.html', context)
    else:
        return HttpResponse("No se pudo autenticar")

def Registro(request):
        return render(request, 'cakehouse/Registro.html')

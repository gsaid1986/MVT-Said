from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(request):
    curso=Curso(nombre="Python",comision=31105)
    curso.save()
    texto=f"Curso creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request, "Appcoder/inicio.html")

def cursos(request):
    return render(request, "Appcoder/cursos.html")

def estudiantes(request):
    return render(request, "Appcoder/estudiantes.html")

def profesores(request):
    return render(request, "Appcoder/profesores.html")

def entregables(request):
    return render(request, "Appcoder/entregables.html")




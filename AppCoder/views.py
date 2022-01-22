from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso

# Create your views here.

from AppCoder.models import Curso, Profesor

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    #curso = Curso(nombre="Desarrollo web", camada="19881")
    #curso.save()
    #documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"

    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request,'AppCoder/estudiantes.html')

def entregables(request):
    return render(request,'AppCoder/entregables.html')

def cursoFormulario(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST) #aqui me llega toda la informacion del html

        print(miFormulario)

        if miFormulario.is_valid: #si paso la validacion de django

            informacion = miFormulario.cleaned_data
            
            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "AppCoder/inicio.html") #vuelvo al inicio o a donde necesite

    else:

        miFormulario = CursoFormulario() #Formulario vacio para construir el HTML. Esto en caso de no pasar la validación
    
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})
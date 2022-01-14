from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

from AppCoder.models import Curso

def curso(self):
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)
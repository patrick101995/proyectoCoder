from django import forms

class CursoFormulario(forms.Form):

    #especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()
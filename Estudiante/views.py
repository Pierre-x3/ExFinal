from django.shortcuts import render, HttpResponse, redirect
from Estudiante.models import Curso
from Estudiante.models import Carrera


# Create your views here.

def index(request):


    return render(request, 'index.html')

def cursos(request):
    campos=Curso._meta.fields
    cursos=Curso.objects.all()
    return render(request,"cursos.html",{
        'campos':campos,
        'cursos':cursos,
        'titulo': 'Listado de cursos',
        'tituloprincipal': 'Cursos'
    })

def eliminar_curso(request,id):
    curso=Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')

def consultas(request):


    return render(request, 'consultas.html')

def carreras(request):
    campos=Carrera._meta.fields
    carreras=Carrera.objects.all()

    return render(request, 'carreras.html',{
          'campos':campos,
        'carreras':carreras,
        'titulo': 'Listado de carreras',
        'tituloprincipal': 'Carreras'
    })

def eliminar_carrera(request,id):
    carrera=Carrera.objects.get(pk=id)
    carrera.delete()
    return redirect('carreras')


def estudiantes(request):


    return render(request, 'estudiantes.html')
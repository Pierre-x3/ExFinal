from django.db import models

# Create your models here.

class Curso(models.Model):
    # Evitamos poner "idcurso" debido a que Django.db crea un campo llamado id por defecto
    codigo=models.CharField(max_length=11)
    nombre=models.CharField(max_length=100)
    horas=models.FloatField()
    creditos=models.FloatField()
    estado=models.CharField(max_length=1)

class Carrera(models.Model):
    # Evitamos poner "idcarrera" debido a que Django.db crea un campo llamado id por defecto
    nombre=models.CharField(max_length=100)
    nombrecorto=models.CharField(max_length=5)
    fecha_fundacion=models.DateField()
    estado=models.CharField(max_length=1) 


class Estudiantes(models.Model):
    # Evitamos poner "idestudiante" debido a que Django.db crea un campo llamado id por defecto
    codigo=models.CharField(max_length=11)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    dni=models.CharField(max_length=8)
    direccion=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField()
    estado=models.CharField(max_length=1)

    
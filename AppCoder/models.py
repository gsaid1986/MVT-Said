from django.db import models

# Create your models here.
#Curso es un modelo, hereda de Model
#con el modelo creo objetos que seran guardados en la base de datos

class Curso(models.Model): 
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class Estudiante(models.Model): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Profesor(models.Model): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

class Entregables(models.Model): 
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()



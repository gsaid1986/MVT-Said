from django.db import models

# Create your models here.
#Curso es un modelo, hereda de Model
#con el modelo creo objetos que seran guardados en la base de datos

class Curso(models.Model): 
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.comision)

class Estudiante(models.Model): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido

class Profesor(models.Model): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

class Entregables(models.Model): 
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()





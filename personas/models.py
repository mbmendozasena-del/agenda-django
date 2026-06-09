from django.db import models

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Persona(models.Model):
    documento = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    fnacimiento = models.DateField()
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
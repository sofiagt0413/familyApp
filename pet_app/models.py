from django.db import models

# Create your models here.
class Pet(models.Model):
    nombre = models.CharField(max_length = 80)
    tipo = models.CharField(max_length = 50)
    raza = models.CharField(max_length = 50)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return f"nombre: {self.nombre}, tipo: {self.tipo}, raza: {self.raza}, edad: {self.edad}"
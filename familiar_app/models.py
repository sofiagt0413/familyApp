from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length = 80)
    altura = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        return f"nombre: {self.nombre}, altura: {self.altura}, fecha de nacimiento: {self.fecha_nacimiento}"
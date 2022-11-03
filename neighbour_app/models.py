from django.db import models

# Create your models here.
class Neighbour(models.Model):
    nombre = models.CharField(max_length = 80)
    barrio = models.CharField(max_length = 50)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return f"nombre: {self.nombre}, barrio: {self.barrio}, edad: {self.edad}"
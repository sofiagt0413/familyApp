from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
# class Pet(models.Model):
#     nombre = models.CharField(max_length = 80)
#     tipo = models.CharField(max_length = 50)
#     raza = models.CharField(max_length = 50)
#     edad = models.IntegerField()

#     def __str__(self) -> str:
#         return f"nombre: {self.nombre}, tipo: {self.tipo}, raza: {self.raza}, edad: {self.edad}"

class Pet(models.Model):
    titulo = models.CharField(max_length=40, null=False, blank=False)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    imagen = models.ImageField(upload_to='pet', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "titulo",
            "nombre",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Titulo: {self.titulo} | nombre: {self.nombre}"


class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

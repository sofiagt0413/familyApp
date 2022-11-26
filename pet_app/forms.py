from django import forms

from pet_app.models import Pet

# class petForm(forms.Form):

#     nombre = forms.CharField(
#         label="Nombre",
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Nombre de la mascota",
#                 "required": "True",
#             }
#         ),
#     )

#     tipo = forms.ChoiceField(
#         label="Tipo",
#         required=True,
#         choices=[('perro','Perro'), ('gato','Gato'), ('tortuga', 'Tortuga'), ('loro','Loro'), ('otro', 'Otro')],
#         widget=forms.Select(
#             attrs={
#                 "class": "form-select",
#                 "placeholder": "tipo: perro, gato, loro....",
#                 "required": "True",
#             }
#         ),
#     )

#     raza = forms.CharField(
#         label="Raza",
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Raza",
#                 "required": "True",
#             }
#         ),
#     )

#     edad = forms.IntegerField(
#         label="Edad",
#         required=True,
#         widget=forms.NumberInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Edad",
#                 "required": "True",
#             }
#         ),
#     )


class PetForm(forms.ModelForm):

    imagen = forms.ImageField()

    titulo = forms.CharField(
        label="titulo del post",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-name",
                "placeholder": "titulo publicacion",
                "required": "True",
            }
        ),
    )

    nombre = forms.CharField(
        label="Nombre de la mascota",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-name",
                "placeholder": "Nombre de la mascota",
                "required": "True",
            }
        ),
    )

    descripcion = forms.CharField(
        label="Descripción:",
        required=False,
        widget=forms.Textarea(
            attrs={
                "required": "True",
            }
        ),
    )


    class Meta:
        model = Pet
        fields = ["titulo", "nombre", "descripcion", "imagen"]


class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style": "min-width: 100%",
            }
        ),
    )

from django import forms

class petForm(forms.Form):

    nombre = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nombre de la mascota",
                "required": "True",
            }
        ),
    )

    tipo = forms.ChoiceField(
        label="Tipo",
        required=True,
        choices=[('perro','Perro'), ('gato','Gato'), ('tortuga', 'Tortuga'), ('loro','Loro'), ('otro', 'Otro')],
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "placeholder": "tipo: perro, gato, loro....",
                "required": "True",
            }
        ),
    )

    raza = forms.CharField(
        label="Raza",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Raza",
                "required": "True",
            }
        ),
    )

    edad = forms.IntegerField(
        label="Edad",
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Edad",
                "required": "True",
            }
        ),
    )

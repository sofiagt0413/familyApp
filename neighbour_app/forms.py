from django import forms

class neighbourForm(forms.Form):

    nombre = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nombre del vecino",
                "required": "True",
            }
        ),
    )

    barrio = forms.CharField(
        label="Barrio",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Barrio donde vive",
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



from django import forms


class FamiliarForm(forms.Form):

    nombre = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nombre del familiar",
                "required": "True",
            }
        ),
    )

    altura = forms.IntegerField(
        label="Altura:",
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Altura en cm",
                "required": "True",
            }
        ),
    )

    fecha_nacimiento = forms.DateField(
        label="Fecha Nacimiento",
        required=True,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "required": "True",
            }
        )
    )



from django.shortcuts import render
from familiar_app.forms import FamiliarForm
from familiar_app.models import Familiar
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def familiars(request):
    familiar = Familiar.objects.all()
    familiars = {"familiars": familiar}
    return render(
        request=request,
        context=familiars,
        template_name="familiar_app/familiar-list.html",
    )

@login_required
def create_familiar(request):
    if request.method == "POST":
        familiar_form = FamiliarForm(request.POST)
        if familiar_form.is_valid():
            data = familiar_form.cleaned_data
            actual_objects = Familiar.objects.filter(
                nombre=data["nombre"], fecha_nacimiento=data["fecha_nacimiento"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El Familiar {data['nombre']} ya está creado",
                )
            else:
                course = Familiar(
                    nombre=data["nombre"],
                    altura=data["altura"],
                    fecha_nacimiento=data["fecha_nacimiento"],
                    )
                course.save()
                messages.success(
                    request,
                    f"Familiar {data['nombre']} creado exitosamente!",
                )

            familiar = Familiar.objects.all()
            familiars = {"familiars": familiar}
            return render(
                request=request,
                context=familiars,
                template_name="familiar_app/familiar-list.html",
            )

    familiar_form = FamiliarForm(request.POST)
    context_dict = {"form": familiar_form}
    return render(
        request=request,
        context=context_dict,
        template_name="familiar_app/familiar-form.html",
    )

from django.shortcuts import render
from django.contrib import messages
from neighbour_app.forms import neighbourForm
from neighbour_app.models import Neighbour
from django.contrib.auth.decorators import login_required

# Create your views here.
def neighbours(request):
    neighbour = Neighbour.objects.all()
    neighbours = {"neighbours": neighbour}
    return render(
        request=request,
        context=neighbours,
        template_name="neighbour_app/neighbour-list.html",
    )

@login_required
def create_neighbour(request):
    if request.method == "POST":
        neighbour_form = neighbourForm(request.POST)
        if neighbour_form.is_valid():
            data = neighbour_form.cleaned_data
            actual_objects = Neighbour.objects.filter(
                nombre=data["nombre"], barrio=data["barrio"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El vecino {data['nombre']} ya está creado",
                )
            else:
                course = Neighbour(
                    nombre=data["nombre"],
                    barrio=data["barrio"],
                    edad=data["edad"],
                    )
                course.save()
                messages.success(
                    request,
                    f"vecino {data['nombre']} creado exitosamente!",
                )

            neighbour = Neighbour.objects.all()
            neighbours = {"neighbours": neighbour}
            return render(
                request=request,
                context=neighbours,
                template_name="neighbour_app/neighbour-list.html",
            )

    neighbour_form = neighbourForm(request.POST)
    context_dict = {"form": neighbour_form}
    return render(
        request=request,
        context=context_dict,
        template_name="neighbour_app/neighbour-form.html",
    )

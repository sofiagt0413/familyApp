from django.shortcuts import render
from django.contrib import messages
from pet_app.models import Pet
from pet_app.forms import petForm

# Create your views here.
def pets(request):
    pet = Pet.objects.all()
    pets = {"pets": pet}
    return render(
        request=request,
        context=pets,
        template_name="pet_app/pet-list.html",
    )


def create_pet(request):
    if request.method == "POST":
        pet_form = petForm(request.POST)
        if pet_form.is_valid():
            data = pet_form.cleaned_data
            actual_objects = Pet.objects.filter(
                nombre=data["nombre"], tipo=data["tipo"], raza=data["raza"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La mascota {data['nombre']} ya está creada",
                )
            else:
                course = Pet(
                    nombre=data["nombre"],
                    tipo=data["tipo"],
                    raza=data["raza"],
                    edad=data["edad"],
                    )
                course.save()
                messages.success(
                    request,
                    f"La mascota {data['nombre']} creado exitosamente!",
                )

            pet = Pet.objects.all()
            pets = {"pets": pet}
            return render(
                request=request,
                context=pets,
                template_name="pet_app/pet-list.html",
            )

    pet_form = petForm(request.POST)
    context_dict = {"form": pet_form}
    return render(
        request=request,
        context=context_dict,
        template_name="pet_app/pet-form.html",
    )

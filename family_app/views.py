from django.shortcuts import render
from django.contrib import messages
from family_app.forms import PersonForm
from family_app.models import Person

# Create your views here.
def persons(request):
    persons = Person.objects.all()

    context_dict = {"persons": persons}
    return render(
        request=request,
        context=context_dict,
        template_name="family_app/person-list.html",
    )


def create_person(request):
    if request.method == "POST":
        course_form = PersonForm(request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            actual_objects = Person.objects.filter(
                name=data["name"], code=data["code"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El curso {data['name']} - {data['code']} ya está creado",
                )
            else:
                course = Person(name=data["name"], code=data["code"])
                course.save()
                messages.success(
                    request,
                    f"Curso {data['name']} - {data['code']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"persons": Person.objects.all()},
                template_name="persons/person_list.html",
            )

    course_form = Person(request.POST)
    context_dict = {"form": course_form}
    return render(
        request=request,
        context=context_dict,
        template_name="person/course_form.html",
    )

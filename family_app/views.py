from django.shortcuts import render
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
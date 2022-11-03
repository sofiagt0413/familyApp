from django.shortcuts import render
from familiar_app.models import Familiar
from django.db.models import Q

# Create your views here.
def search(request):
    context_dict = dict()
    if(request.GET.get("search_param", False)):
        search_param = request.GET["search_param"]
        if search_param:
            query = Q(nombre__contains=search_param)
            # query.add(Q(code__contains=search_param), Q.OR)
            familiars = Familiar.objects.filter(query)
            context_dict.update(
                {
                    "familiars": familiars,
                    "search_param": search_param,
                }
            )
    return render(
        request=request,
        context=context_dict,
        template_name="home_app/home.html",
    )

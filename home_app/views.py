from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request=request,
        context={},
        template_name="home_app/home.html",
    )
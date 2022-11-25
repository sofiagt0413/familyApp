import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.shortcuts import render

from home_app.forms import AvatarForm
from home_app.forms import UserRegisterForm
from home_app.forms import UserUpdateForm
from home_app.models import Avatar

from familiar_app.models import Familiar


# Create your views here.
def search(request):
    context_dict = dict()
    if request.GET.get("search_param", False):
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


def about(request):
    return render(
        request=request,
        template_name="home_app/about.html",
    )


def register(request):
    form = UserRegisterForm(request.POST) if request.POST else UserRegisterForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("login")

    return render(
        request=request,
        context={"form": form},
        template_name="registration/register.html",
    )


@login_required
def user_update(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home_app:home")

    form = UserUpdateForm(model_to_dict(user))

    avatar_url = None
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars:
        avatar_url = avatars[0].image.url

    context = {"form": form, "avatar_url": avatar_url}
    return render(
        request=request,
        context=context,
        template_name="registration/user_form.html",
    )


@login_required
def avatar_load(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid and len(request.FILES) != 0:
            image = request.FILES["image"]
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect("home_app:home")

    form = AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="home_app/avatar_form.html",
    )

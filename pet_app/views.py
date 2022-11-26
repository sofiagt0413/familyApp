from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from pet_app.models import Comment, Pet
from pet_app.forms import CommentForm, PetForm

class PetListView(ListView):
    model = Pet
    paginate_by = 3

class PetDetailView(DetailView):
    model = Pet
    template_name = "pet_app/pet_detail.html"
    fields = ["titulo", "nombre", "descripcion", "imagen"]
    
    def get(self, request, pk):
        pet = Pet.objects.get(id=pk)
        comments = Comment.objects.filter(pet=pet).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "pet": pet,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    success_url = reverse_lazy("pet_app:pet-list")

    form_class = PetForm
    # fields = ["name", "code", "description", "image"]

    def form_valid(self, form):
        """Filter to avoid duplicate courses"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Pet.objects.filter(
            titulo=data["titulo"], nombre=data["nombre"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La publicacion {data['titulo']} - de la mascota {data['nombre']} ya existe",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"La publicacion {data['titulo']} - de la mascota {data['nombre']} ha sido creada exitosamente!",
            )
            return super().form_valid(form)


class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetForm
    #fields = ["titulo", "nombre", "descripcion", "imagen"]

    def get_success_url(self):
        pet_id = self.kwargs["pk"]
        return reverse_lazy("pet_app:pet-detail", kwargs={"pk": pet_id})

class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = reverse_lazy("pet_app:pet-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        pet = get_object_or_404(Pet, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, pet=pet
        )
        comment.save()
        return redirect(reverse("pet_app:pet-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        pet = self.object.pet
        return reverse("pet_app:pet-detail", kwargs={"pk": pet.id})


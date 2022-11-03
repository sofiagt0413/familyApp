from django.urls import path

from pet_app import views

app_name = "pet_app"
urlpatterns = [
    path("pets", views.pets, name="pet-list"),
    path("pet/add", views.create_pet, name="pet-add"),
]
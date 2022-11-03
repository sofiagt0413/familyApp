from django.urls import path

from familiar_app import views

app_name = "familiar_app"
urlpatterns = [
    path("familiars", views.familiars, name="familiar-list"),
    path("familiar/add", views.create_familiar, name="familiar-add"),
]
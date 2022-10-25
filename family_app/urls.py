from django.urls import path

from family_app import views

app_name = "family_app"
urlpatterns = [
    path("persons", views.persons, name="person-list"),
]
from django.urls import path

from neighbour_app import views

app_name = "neighbour_app"
urlpatterns = [
    path("neighbours", views.neighbours, name="neighbour-list"),
    path("neighbour/add", views.create_neighbour, name="neighbour-add"),
]
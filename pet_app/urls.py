from django.urls import path

from pet_app import views

app_name = "pet_app"
urlpatterns = [
    #mascotas
    path("pets/", views.PetListView.as_view(), name="pet-list"),
    path("pet/add/", views.PetCreateView.as_view(), name="pet-add"),
    path("pet/<int:pk>/detail/", views.PetDetailView.as_view(), name="pet-detail"),
    path("pet/<int:pk>/update/", views.PetUpdateView.as_view(), name="pet-update"),
    path("pet/<int:pk>/delete/", views.PetDeleteView.as_view(), name="pet-delete"),

    #comentarios
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]
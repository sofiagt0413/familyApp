from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy


from home_app import views

app_name = "home_app"
urlpatterns = [
    path("", views.search, name="home"),
    path("about", views.about, name="about"),

    path('avatar/load', views.avatar_load, name='avatar-load'),
    path("register/", views.register, name="user-register"),
    path('register/update/', views.user_update, name='user-update'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url=reverse_lazy("home_app:password-change-done")
        ),
        name="password-change"
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/change-password-done.html'
        ),
        name="password-change-done"
    ),
]
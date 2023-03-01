from django.urls import path
from canoe_club import views

app_name = "rango"

urlpatterns = [
    path("", views.index, name ="index"),
    path("socials/",views.socials, name ="socails"),
    path("about/", views.about, name ="about"),
]
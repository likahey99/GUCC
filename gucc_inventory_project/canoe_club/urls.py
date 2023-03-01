from django.urls import path
from canoe_club import views
from django.conf.urls import url


app_name = 'canoe_club'

urlpatterns = [
    path("", views.index, name ="index"),
    path("socials/",views.socials, name ="socails"),
    path("about/", views.about, name ="about"),
    path('login/', views.user_login, name='login'),
    #path (login/profile),
    #path (login/profile/change_password),
    #path (login/profile/edit_profile),
    path('maintenance_shed/', views.maintenance_shed, name='maintenance_shed'),
    #path(maintenance_shed/item),
    #path(maintenance_shed/item/move_item),
    path('main_shed/', views.main_shed, name='main_shed'),
    #path(main_shed/item/add_item),
    #path(main_shed/item/move_shed),
    path('socials/', views.socials, name='socials'),
    #path (socials/add_social),
    path('trips/', views.trips, name='trips'),
    #path (trips/trip)
    #path (trips/trip/member)
    #path (trips/trip/add_member)
    #path (trips/trip/add_trip)
    ]

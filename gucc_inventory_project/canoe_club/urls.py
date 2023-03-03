from django.urls import path
from canoe_club import views
from django.conf.urls import url


app_name = 'canoe_club'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),
    path('login/profile/', views.user_profile, name='profile'),
    path('login/profile/change_password/', views.change_password, name='change_password'),
    path('login/profile/edit_profile/', views.edit_profile, name='edit_profile'),
    

    path('maintenance_shed/', views.maintenance_shed, name='maintenance_shed'),
    path('maintenance_shed/item/', views.maintenance_shed_item, name='maintenance_shed_item'),
    path('maintenance_shed/item/move_item/', views.move_item, name='move_item'),

    path('main_shed/', views.main_shed, name='main_shed'),
    path('main_shed/item/add_item/', views.add_item, name='add_item'),
    path('main_shed/item/move_shed/', views.move_shed, name='move_shed'),

    path('socials/', views.socials, name='socials'),
    path('socials/add_social/', views.add_social, name='add_social'),

    path('trips/', views.trips, name='trips'),
    path('trips/trip/', views.trip, name='trip'),
    path('trips/trip/member/', views.trip_member, name='trip_member'),
    path('trips/trip/add_member/', views.add_trip_member, name='add_trip_member'),
    path('trips/trip/add_trip/', views.add_trip, name='add_trip'),

    ] 
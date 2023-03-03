from django.urls import path
from canoe_club import views
from django.conf.urls import url
urlpatterns = [
    path("", views.index, name ="index"), #has view
    path("about/", views.about, name ="about"), #has view
    path('register/', views.register, name='register'), #has view

    path('login/', views.user_login, name='login'), #has view
    path('login/profile/', views.user_profile, name='profile'), # has view
    path('login/profile/change_password/', views.change_password, name='change_password'), #has view
    path('login/profile/edit_profile/', views.edit_profile, name='edit_profile'), #has edit_profile


    path('maintenance_shed/', views.maintenance_shed, name='maintenance_shed'), #has view
    #in design spec kit was item but we have changed it here
    path('maintenance_shed/kit/', views.maintenance_shed_kit, name='maintenance_shed_kit'), #has view
    path('maintenance_shed/kit/move_kit/', views.move_kit, name='move_kit'),#has view

    path('main_shed/', views.main_shed, name='main_shed'), #has view
    path('main_shed/kit/add_kit/', views.add_kit, name='add_kit'), #has
    path('main_shed/kit/remove_kit/', views.remove_kit, name='remove_kit'), #has view
    path('main_shed/kit/move_shed/', views.move_shed, name='move_shed'), #has view


    path('socials/', views.socials, name='socials'), #has view
    path('socials/add_social/', views.add_social, name='add_social'),#has view
    path('socials/remove_social/', views.remove_social, name='remove_social'),#has view

    path('trips/', views.trips, name='trips'), #has view
    path('trips/trip/', views.trip, name='trip'), #has view
    path('trips/trip/member/', views.trip_member, name='trip_member'), #has view
    path('trips/trip/add_member/', views.add_trip_member, name='add_trip_member'),#has view
    path('trips/trip/remove_member/', views.remove_trip_member, name='remove_trip_member'),#has view
    path('trips/trip/add_trip/', views.add_trip, name='add_trip'),#has view
    path('trips/trip/remove_trip/', views.remove_trip, name='remove_trip'),#has view


    ]


app_name = 'canoe_club'


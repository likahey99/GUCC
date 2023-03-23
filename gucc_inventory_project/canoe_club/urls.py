from django.urls import path
from canoe_club import views
from django.conf.urls import url

app_name = "canoe_club"
urlpatterns = [
    path("", views.index, name ="index"),
    path("about/", views.about, name ="about"),
    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<username>/', views.user_profile, name='profile'),
    path('profile/settings/change_password/', views.change_password, name='change_password'),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('reset_password/<uidb64>/', views.password_reset_confirm, name ="password_reset_confirm"),
    path('profile/settings/edit_profile/', views.edit_profile, name='edit_profile'),

    path('maintenance_shed/', views.maintenance_shed, name='maintenance_shed'),
    path('maintenance_shed/<kit_name_slug>/', views.kit, name='maintenance_shed_kit'),

    path('main_shed/', views.main_shed, name='main_shed'),
    path('main_shed/kit/<kit_name_slug>/', views.kit, name='main_shed_kit'),
    path('main_shed/add_kit/', views.add_kit, name='add_kit'),
    path('main_shed/kit/remove_kit/', views.remove_kit, name='remove_kit'),

    path('socials/', views.socials, name='socials'),
    path('socials/add_social/', views.add_social, name='add_social'),
    path('socials/<social_name_slug>', views.social, name='social'),
    path('socials/<social_name_slug>/remove_social/', views.remove_social, name='remove_social'),

    path('trips/', views.trips, name='trips'),
    path('trips/add_trip/', views.add_trip, name='add_trip'),
    path('trips/<trip_name_slug>/', views.trip, name='trip'),
    path('trips/<trip_name_slug>/remove_trip/', views.remove_trip, name='remove_trip'),

    path('trips/trip/add_member/', views.add_trip_member, name='add_trip_member'),
    # path('trips/trip/member/', views.trip_member, name='trip_member'),
    path('trips/trip/remove_member/', views.remove_trip_member, name='remove_trip_member'),



    ]




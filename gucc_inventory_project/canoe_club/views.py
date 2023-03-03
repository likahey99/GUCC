from django.shortcuts import render
from canoe_club.models import Trip, Social, Kit
import datetime

def index(request):
    today = datetime.datetime.today()
    trips_list = Trip.objects.filter(date__gte=today).order_by("date")[:5]
    social_list = Social.objects.filter(date__gte=today).order_by("date")[:5]

    print(social_list)
    context_dixt = {}
    context_dixt["trips"] = trips_list
    context_dixt["socials"] = social_list
    return render(request, 'canoe_club/index.html', context_dixt)

# Create your views here.

def about(request):
    return render(request, 'canoe_club/about.html')


def main_shed(request):
    return render(request, 'canoe_club/main_shed.html')

def add_kit(request):
    return render(request, 'canoe_club/main_shed/kit/add_kit.html')

def remove_kit(request):
    return render(request, 'canoe_club/main_shed/kit/remove_kit.html')

def move_shed(request):
    return render(request, 'canoe_club/main_shed/kit/move_shed.html')


def maintenance_shed(request):
    return render(request, 'canoe_club/maintenance_shed.html')

def maintenance_shed(request):
    return render(request, 'canoe_club/maintenance_shed.html')

def kit(request, kit_name_slug):

    try:
        kit = Kit.objects.get(slug = kit_name_slug)
        context_dict["kit"] = kit

    except Kit.DoesNotExist:
        context_dict["kit"] = None

    return render(request, "canoe_club/kit.html", context_dict)

def move_kit(request, kit_name_slug):
    return render(request, "canoe_club/kit/move_kit.html")

def user_login(request):
    return render(request, 'canoe_club/login.html')

def user_profile(request):
    return render(request, 'canoe_club/login/profile.html')

def change_password(request):
    return render(request, 'canoe_club/login/profile/change_password.html')

def edit_profile(request):
    return render(request, 'canoe_club/login/profile/edit_profile.html')

def register(request):
    return render(request, 'canoe_club/register.html')

def socials(request):
    today = datetime.datetime.today()
    social_list = Social.objects.order_by("-date")
    context_dixt = {}
    context_dixt["socials"] = social_list
    return render(request, "canoe_club/socials.html", context_dixt)

def add_social(request):
    return render(request, "canoe_club/socials/add_social.html")

def remove_social(request):
    return render(request, "canoe_club/socials/remove_social.html")


def trips(request):
    today = datetime.datetime.today()
    trip_list = Trip.objects.order_by("-date")
    context_dixt = {}
    context_dixt["trips"] = trip_list
    return render(request, "canoe_club/trips.html", context_dixt)


def trip(request, trip_name_slug):

    try:
        trip = Trip.objects.get(slug = kit_name_slug)
        context_dict["trip"] = trip

    except Trip.DoesNotExist:
        context_dict["trip"] = None

    return render(request, "canoe_club/trip.html", context_dict)

def trip_member(request):
    return render(request, "canoe_club/trips/trip/member.html")

def add_trip_member(request):
    return render(request, "canoe_club/trips/trip/member/add_member.html")

def remove_trip_member(request):
    return render(request, "canoe_club/trips/trip/member/remove_member.html")

def add_trip(request):
    return render(request, "canoe_club/trips/trip/add_trip.html")

def remove_trip(request):
    return render(request, "canoe_club/trips/trip/remove_trip.html")






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


def maintenance_shed(request):
    return render(request, 'canoe_club/maintenance_shed.html')


def trips(request):
    return render(request, 'canoe_club/trips.html')


def user_login(request):
    return render(request, 'canoe_club/login.html')


def register(request):
    return render(request, 'canoe_club/register.html')

def socials(request):
    today = datetime.datetime.today()
    social_list = Social.objects.order_by("-date")
    context_dixt = {}
    context_dixt["socials"] = social_list
    return render(request, "canoe_club/socials.html", context_dixt)

def trips(request):
    today = datetime.datetime.today()
    trip_list = Trip.objects.order_by("-date")
    context_dixt = {}
    context_dixt["trips"] = trip_list
    return render(request, "canoe_club/trip.html", context_dixt)


def kit(request, kit_name_slug):

    try:
        kit = Kit.objects.get(slug = kit_name_slug)
        context_dict["kit"] = kit

    except Kit.DoesNotExist:
        context_dict["kit"] = None

    return render(request, "canoe_club/kit.html", context_dict)

def trip(request, trip_name_slug):

    try:
        trip = Trip.objects.get(slug = kit_name_slug)
        context_dict["trip"] = trip

    except Trip.DoesNotExist:
        context_dict["trip"] = None

    return render(request, "canoe_club/trip.html", context_dict)

def about(request):
    return render(request, "canoe_club/about.html", {})

#  a change
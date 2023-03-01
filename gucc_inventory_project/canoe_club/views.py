from django.shortcuts import render
from canoe_club.models import Trip, Social
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

def socials(request):
    today = datetime.datetime.today()
    social_list = Social.objects.order_by("-date")
    context_dixt = {}
    context_dixt["socials"] = social_list
    return render(request, "canoe_club/socials.html", context_dixt)
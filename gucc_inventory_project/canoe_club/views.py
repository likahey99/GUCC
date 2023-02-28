from django.shortcuts import render
from canoe_club.models import Trip, Social

def index(request):
    trips_list = Trip.objects.order_by("-date")[:5]
    social_list = Social.objects.order_by("-date")[:5]
    context_dixt = {}
    context_dixt["trips"] = trips_list
    context_dixt["socials"] = social_list
    return render(request, 'canoe_club/index.html', context_dixt)
# Create your views here.

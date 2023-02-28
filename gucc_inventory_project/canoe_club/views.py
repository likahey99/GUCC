from django.shortcuts import render
from canoe_club.models import Trip, Social
import datetime

def index(request):
    handleTime(Trip)
    handleTime(Social)
    trips_list = Trip.objects.order_by("-date")[:5]
    social_list = Social.objects.order_by("-date")[:5]

    context_dixt = {}
    context_dixt["trips"] = trips_list
    context_dixt["socials"] = social_list
    return render(request, 'canoe_club/index.html', context_dixt)
# Create your views here.

def handleTime(model):
    model.objects.filter(date=datetime.now() - timedelta(days=1)).delete()
    return
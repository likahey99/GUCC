from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("this is the index pag")
# Create your views here.

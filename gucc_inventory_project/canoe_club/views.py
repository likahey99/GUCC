from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("this is the index pag")
    return render(request, 'canoe_club/index.html')
# Create your views here.

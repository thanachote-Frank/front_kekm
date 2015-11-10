from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def select_schedule(request):

    return render(request, 'select_schedule.html')
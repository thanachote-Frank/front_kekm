from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def workout_schedule(request):

    return render(request, 'workout_schedule.html')
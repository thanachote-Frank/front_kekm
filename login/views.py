from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    # print '000'
    # return HttpResponse('hello')
    return render(request, 'login.html')
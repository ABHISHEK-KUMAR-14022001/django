from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hellow, World!")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hellow, about")

def contact(request):
    return HttpResponse("Hellow, contact")
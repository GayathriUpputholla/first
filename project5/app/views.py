from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def home1(request):
    return render(request,'home1.html')  
from django.http import HttpResponse
def sree(request):
    return HttpResponse('THIS IS MY SECOND TEMPLATE')
def ram(request):
    return HttpResponse('RAM IS VERRY GOODBOY')   
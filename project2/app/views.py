


from  django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('This is my first fbv')
def second(request):
    return HttpResponse('This is my second fbv')   


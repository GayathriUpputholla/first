from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'gayathri','age':21}
    return render(request,'wish.html',context=d)

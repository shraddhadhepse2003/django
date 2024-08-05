from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def first(request):
    return render(request,'first.html')

def second(request):
    return render(request,'second.html')


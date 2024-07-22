from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def firstpage(request):
    return render(request,'firstpage.html')
from django.shortcuts import render,HttpResponse

def home (request):
    return render(request,'home.html')

def firstpage(request):
    return render(request,'firstpage.html')

def secondpage(request):
    return render(request,'secondpage.html')

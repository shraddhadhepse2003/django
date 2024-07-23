from django.shortcuts import render,HttpResponse,redirect
from .models import Emp

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_emp(request):
    if request.method == 'POST':
        name=request.POST.get('myname') 
        age=request.POST.get('myage')
        address=request.POST.get('myaddress')

        e=Emp()  
        e.name=name
        e.age=age
        e.address=address
        e.save()
        return redirect('/')
    else:
        return render(request,'addemp.html')
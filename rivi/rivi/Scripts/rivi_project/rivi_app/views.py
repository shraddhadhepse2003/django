from django.shortcuts import render,HttpResponse,redirect
from .models import Emp,AccountForm

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

def add_account(request):
    if request.method=="POST":
        f=AccountForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=AccountForm
        context={'form':f}
        return render(request,'addaccount.html',context)
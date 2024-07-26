from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html')

def register_view(request):
    if request.method=="POST":
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'register.html',context)

from .models import LoginForm
def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)

        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            f=LoginForm
            context={'form':f}
            return render(request,'login.html',context)
    else:
        f=LoginForm
        context={'form':f}
        return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')


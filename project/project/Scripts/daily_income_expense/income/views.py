from django.shortcuts import render,redirect
from .models import Income,IncomeForm

# Create your views here.
def add_income(request):
    if request.method=='POST':
        f=IncomeForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=IncomeForm
        context={'form':f}
        return render(request,'addincome.html',context)

def income_list(request):
    inc=Income.objects.all()
    context={'inclist':inc}
    return render(request,'incomelist.html',context)

def delete_income(request,inid):
    inc=Income.objects.get(id=inid)
    inc.delete()
    return redirect('/incomelist')

def edit_income(request,inid):
    inc=Income.objects.get(id=inid)
    if request.method=="POST":
        f=IncomeForm(request.POST,instance=inc)
        f.save()
        return redirect('/incomelist')
    else:
        f=IncomeForm(instance=inc)
        context={'form':f}
        return render(request,'addincome.html',context)
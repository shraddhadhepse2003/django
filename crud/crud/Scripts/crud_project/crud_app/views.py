from django.shortcuts import render,HttpResponse,redirect
from .models import Emp,EmpForm,Account,AccountForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def add_emp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=EmpForm
        context={'form':f}
        return render(request,'addemp.html',context)

def add_account(request):
    if request.method=='POST':
        f=AccountForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=AccountForm
        context={'form':f}
        return render(request,'addaccount.html',context)

def emp_list(request):
    emp1=Emp.objects.all()
    context={'elist':emp1}
    return render(request,'emplist.html',context)

def delete_emp(request):
    eid=request.GET.get('id')
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/emplist')

def delete2_emp(request,eid):
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/emplist')

def edit_emp(request,eid):
    emp=Emp.objects.get(id=eid)
    if request.method=='POST':
        f=EmpForm(request.POST,instance=emp)
        f.save()
        return redirect('/emplist')
    else:
        f=EmpForm(instance=emp)
        context={'form':f}
        return render(request,'addemp.html',context)

def accou_list(request):
    accou1=Account.objects.all()
    context={'alist':accou1}
    return render(request,'accoulist.html',context)

def delete_accou(request):
    aid=request.GET.get('id')
    acc=Account.objects.get(id=aid)
    acc.delete()
    return redirect('/accoulist')

def delete2_accou(request,aid):
    acc=Account.objects.get(id=aid)
    acc.delete()
    return redirect('/accoulist')

def edit_accou(request,aid):
    acc=Account.objects.get(id=aid)
    if request.method=='POST':
        f=AccountForm(request.POST,instance=acc)
        f.save()
        return redirect('/accoulist')
    else:
        f=AccountForm(instance=acc)
        context={'form':f}
        return render(request,'addaccount.html',context)
from django.shortcuts import render,redirect
from .models import Income,IncomeForm
from django.contrib.auth.models import User

# Create your views here.
def add_income(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        #f=IncomeForm(request.POST)
        income=request.POST.get('income')
        income_type=request.POST.get('income_type')
        income_date=request.POST.get('income_date')
        description=request.POST.get('description')
        inc=Income()
        inc.income=income
        inc.income_type=income_type
        inc.income_date=income_date
        inc.description=description
        inc.user=User.objects.get(id=uid)
        inc.save()
        return redirect('/')
    else:
        f=IncomeForm
        context={'form':f}
        return render(request,'addincome.html',context)

def income_list(request):
    ##inc=Income.objects.all()
    #uid=request.session.get('uid')
    #inc=Income.objects.filter(user=uid)
    #context={'inc':inc}
    #return render(request,'incomelist.html',context)

    uid=request.session.get('uid')
    inc=Income.objects.filter(user=uid)
    inct=set()
    for i in inc:
        inct.add(i.income_type)
    context={'inc':inc,'inct':inct}
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

def inc_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    inc=Income.objects.filter(user=uid,description__contains=srch)
    context={'inc':inc}
    return render(request,'incomelist.html',context)


def sort_by_income_type(request,inc2):
    uid=request.session.get('uid')
    inc=Income.objects.filter(user=uid)
    inct=set()
    for i in inc:
        inct.add(i.income_type)
        inc=Income.objects.filter(user=uid,income_type=inc2)
    context={'inc':inc,'inct':inct}
    return render(request,'incomelist.html',context)
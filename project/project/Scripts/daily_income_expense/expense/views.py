from django.shortcuts import render,HttpResponse,redirect
from .models import Expense,ExpenseForm
from django.contrib.auth.models import User

# Create your views here.
def add_expense(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        #f=ExpenseForm(request.POST)
        expense=request.POST.get('expense')
        expense_type=request.POST.get('expense_type')
        description=request.POST.get('description')
        exp=Expense()
        exp.expense=expense
        exp.expense_type=expense_type
        exp.description=description
        exp.user=User.objects.get(id=uid)
        exp.save()
        return redirect('/')
    else:
        f=ExpenseForm
        context={'form':f}
        return render(request,'addexpense.html',context)


def expense_list(request):
    #exp=Expense.objects.all()
    #uid=request.session.get('uid')
    #exp=Expense.objects.filter(user=uid)
    #context={'exp':exp}#exlist
    #return render(request,'expenselist.html',context)

    #exp=Expense.objects.all()
    uid=request.session.get('uid')
    exp=Expense.objects.filter(user=uid)
    expt=set()
    for i in exp:
        expt.add(i.expense_type)
    context={'exp':exp,'expt':expt}
    return render(request,'expenselist.html',context)


def delete_expense(request,eid):
    exp=Expense.objects.get(id=eid)
    exp.delete()
    return redirect('/expenselist')

def edit_expense(request,eid):
    exp=Expense.objects.get(id=eid)
    if request.method=="POST":
        f=ExpenseForm(request.POST,instance=exp)
        f.save()
        return redirect('/expenselist')
    else:
        f=ExpenseForm(instance=exp)
        context={'form':f}
        return render(request,'addexpense.html',context)
    

def exp_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    exp=Expense.objects.filter(user=uid,description__contains=srch)
    context={'exp':exp}
    return render(request,'expenselist.html',context)


def sort_by_expense_type(request,ext2):
    uid=request.session.get('uid')
    exp=Expense.objects.filter(user=uid)
    expt=set()
    for i in exp:
        expt.add(i.expense_type)
        exp=Expense.objects.filter(user=uid,expense_type=ext2)
    context={'exp':exp,'expt':expt}
    return render(request,'expenselist.html',context)

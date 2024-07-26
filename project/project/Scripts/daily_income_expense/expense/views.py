from django.shortcuts import render,HttpResponse,redirect
from .models import Expense,ExpenseForm

# Create your views here.
def add_expense(request):
    if request.method=='POST':
        f=ExpenseForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=ExpenseForm
        context={'form':f}
        return render(request,'addexpense.html',context)


def expense_list(request):
    exp=Expense.objects.all()
    context={'exlist':exp}
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
    
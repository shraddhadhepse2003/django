from django.shortcuts import render,HttpResponse,redirect
from .models import Student,StudentForm,Course,CourseForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_student(request):
    if request.method=='POST':
        f=StudentForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=StudentForm
        context={'form':f}
        return render(request,'addstudent.html',context)

def student_list(request):
    stud=Student.objects.all()
    context={'studlist':stud}
    return render(request,'studentlist.html',context)

def stud_delete(request,sid):
    stud=Student.objects.get(id=sid)
    stud.delete()
    return redirect('/stulist')

def stud_edit(request,sid):
    stud=Student.objects.get(id=sid)
    if request.method=='POST':
        f=StudentForm(request.POST,instance=stud)
        f.save()
        return redirect('/stulist')
    else:
        f=StudentForm(instance=stud)
        context={'form':f}
        return render(request,'addstudent.html',context)

def add_course(request):
    if request.method=='POST':
        f=CourseForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=CourseForm
        context={'form':f}
        return render(request,'addcourse.html',context)

def course_list(request):
    cour=Course.objects.all()
    context={'courselist':cour}
    return render(request,'courselist.html',context)

from django.db import models
from django import forms

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        db_table='student'

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


class Course(models.Model):
    c_name=models.CharField(max_length=30)
    c_fee=models.IntegerField()
    c_duration=models.CharField(max_length=30)
    stud=models.ForeignKey(Student,on_delete=models.CASCADE)

    class Meta:
        db_table='course'

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'


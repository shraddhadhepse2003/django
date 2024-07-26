from django.db import models
from django import forms

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=300)


    class Meta:
        db_table='emp'
    
    def __str__(self):
        return self.name

class Account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=30)
    year=models.IntegerField()
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)

    class Meta:
        db_table='account'

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'
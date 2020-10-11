from django.db import models
import uuid
# Create your models here.
PAYMENT_TYPE = (
    ('CASH','cash'),
    ('CHEQUE','cheque'),
    ('DEMAND DRAFT','demand draft')
)

class Expense(models.Model):
    expid = models.CharField(max_length=10,default=uuid.uuid4)
    expname = models.CharField(max_length=50,null=True,blank=True)
    expmode = models.CharField(max_length=15,choices=PAYMENT_TYPE)
    amount = models.IntegerField(default=0)
    expreason = models.CharField(max_length=50)
    expby = models.CharField(max_length=50,null=True,blank=True)
    expdate = models.DateField()
    detail = models.TextField()
    bankname = models.CharField(default=None,max_length=50,null=True,blank=True)
    chequeordd = models.IntegerField(default=0,null=True,blank=True)
    dateinbank = models.CharField(default=None,null=True,blank=True,max_length=50)

    def __str__(self):
        return self.expname

class Income(models.Model):
    incid = models.CharField(max_length=10,default=uuid.uuid4)
    incname = models.CharField(max_length=50,null=True,blank=True)
    incdate = models.DateField()
    incmode = models.CharField(max_length=15,choices=PAYMENT_TYPE)
    incamt = models.IntegerField(default=0)
    increason = models.CharField(max_length=50)
    incby = models.CharField(max_length=50)
    bankname = models.CharField(max_length=50,null=True,blank=True,default=None)
    chequeordd = models.IntegerField(default=None,null=True,blank=True)
    dateinbank = models.CharField(null=True,blank=True,default=None,max_length=50)

    def __str__(self):
        return self.incname

class Employee(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(null=True,blank=True,max_length=50)
    desination = models.CharField(max_length=50,null=True,blank=True)
    desginkdda = models.CharField(max_length=50,null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.empname

class IncomeType(models.Model):
    typeid = models.IntegerField()
    typename = models.CharField(max_length=50,null=True,blank=True)

class ExpenseType(models.Model):
    etypeid = models.IntegerField()
    etypename = models.CharField(max_length=50,null=True,blank=True)

class Transaction(models.Model):
    bankname = models.CharField(max_length=20,null=True,blank=True)
    mode = models.CharField(max_length=20,blank=True, null=True)
    number = models.IntegerField(default=0)
    amt = models.IntegerField()

    def __str__(self):
        return self.bankname

class Opening(models.Model):
    cashinhand = models.IntegerField(blank=True,null=True)
    cashatbank = models.IntegerField(blank=True,null=True)
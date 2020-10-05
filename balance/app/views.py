from django.shortcuts import render,redirect,get_object_or_404
from .models import(
    Expense,
    Income,
    IncomeType,
    ExpenseType,
    Employee
)
from django.views.generic import View
from django.contrib import messages
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import get_template
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import FloatField
from django.contrib.auth import authenticate,forms
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
import csv
import datetime
from django.template import loader
from django.contrib.auth import user_logged_in
from django.core.exceptions import PermissionDenied
# create your views
def home(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    total = 0 
    tot = 0
    for income in incomes:
        tot += income.incamt

    for expense in expenses:
        total += expense.amount

    context = {
        "tot":tot,
        "total":total
    }
    return render(request,'index.html',context)

def details(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    total = 0 
    tot = 0
    for income in incomes:
        tot += income.incamt

    for expense in expenses:
        total += expense.amount

    context = {
        "tot":tot,
        "total":total
    }
    return render(request,'details.html',context)
    
# income view 
class IncomeView(LoginRequiredMixin,View):
    template_name = "income.html"
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request,*args, **kwargs):
        incomes = Income.objects.all()[:6]
        total = 0
        for income in incomes:
            total += income.incamt

        context = { 
            "incomes":incomes,
            "total":total
        }
        return render(request,self.template_name ,context)

# expense view
class ExpenseView(LoginRequiredMixin,View):
    template_name ="expense.html"
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request):
        expenses = Expense.objects.all()
        tot = 0
        for expense in expenses:
            tot += expense.amount

        

        context = {
            "expenses":expenses,
            "tot":tot
        }   
        return render(request,self.template_name ,context)

class AddincomeView(LoginRequiredMixin,View):
    template_name = 'addincome.html'
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request,incomemode):
        context={
            'incomemode':incomemode
        }
        messages.success(request, f'User is Active, The User can Add Income Details')
        return render(request,self.template_name,context)
    def post(self,request,incomemode):
        data = request.POST
        income = Income()
        income.unique_id =uuid.uuid4()
        income.incname =data['incname']
        income.incdate = data['incdate']
        income.incmode = data['incmode']
        income.incamt = data['incamt']
        income.increason = data['increason']
        income.incby = data['incby']
        income.bankname = data['bankname']
        income.chequeordd = data['chequeordd']
        income.dateinbank = data['dateinbank']
        income.save()
        messages.success(request, f'Income is added successfully!...')
        return redirect("income")
        return render(request,self.template_name)

class AddexpenseView(LoginRequiredMixin,View):
    template_name ="addexpense.html"
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request,expensemode):
        context={
            'expensemode':expensemode
        }
        return render(request,self.template_name,context)
    def post(self,request,expensemode):
        data = request.POST
        expense = Expense()
        expense.unique_id =uuid.uuid4()
        expense.expname =data['expname']
        expense.expdate = data['expdate']
        expense.expmode = data['expmode']
        expense.amount = data['amount']
        expense.expreason = data['expreason']
        expense.expby = data['expby']
        expense.bankname = data['bankname']
        expense.chequeordd = data['chequeordd']
        expense.dateinbank = data['dateinbank']
        expense.detail = data['detail']
        expense.save()
        messages.success(request, f'Expense is added successfully!...')
        return redirect("expense")
        return render(request,self.template_name)

class AddIncomeTypeView(View,LoginRequiredMixin):
    template_name = 'add-income-type.html'
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        data = request.POST
        incometype = IncomeType()
        incometype.typeid = data['typeid']
        incometype.typename = data['typename']
        incometype.save()
        messages.success(request, f'Income Type is added successfully!...')
        return redirect("income-type")
        return render(request,self.template_name)

class AddExpenseTypeView(View,LoginRequiredMixin):
    template_name = 'add-expense-type.html'
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        data = request.POST
        expensetype = ExpenseType()
        expensetype.etypeid = data['etypeid']
        expensetype.etypename = data['etypename']
        expensetype.save()
        messages.success(request, f'Expense Type is added successfully!...')
        return redirect("expense-type")
        return render(request,self.template_name)

class ExpenseDeleteView(View,LoginRequiredMixin):
    def get(self,request,pk):
        expense = Expense.objects.get(pk=pk)
        expense.delete()
        messages.success(request, f'Expense is Deleted successfully!...')
        return redirect("expense")

class IncomeDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        income = Income.objects.get(pk=pk)
        income.delete()
        messages.success(request, f'Income is Deleted successfully!...')
        return redirect("income")

class IncomeUpdateView(View,LoginRequiredMixin):
    template_name = 'update.html'
    def get(self,request,pk):
        income = get_object_or_404(Income,pk=pk)
        context = {
            'incname':income.incname,
            'incdate':income.incdate,
            'incmode':income.incmode,
            'incamt':income.incamt,
            'increason':income.increason,
            'incby':income.incby,
            'bankname':income.bankname,
            'chequeordd':income.chequeordd,
            'dateinbank':income.dateinbank
        }
        return render(request,self.template_name,context)

    def post(self,request,pk):
        income = get_object_or_404(Income,pk=pk)
        data = request.POST
        income.incname = data['incname']
        income.incdate = data['incdate']
        income.incmode = data['incmode']
        income.incamt = data['incamt']
        income.increason = data['increason']
        income.incby = data['incby']
        income.bankname = data['bankname']
        income.chequeordd = data['chequeordd']
        income.dateinbank = data['dateinbank']
        income.save()
        return redirect('income')
        return render(request,self.template_name)  

class ExpenseUpdateView(View,LoginRequiredMixin):
    template_name = 'update-expense.html'
    def get(self,request,pk):
        expense = get_object_or_404(Expense,pk=pk)
        context = {
            'expname':expense.expname,
            'expdate':expense.expdate,
            'expmode':expense.expmode,
            'amount':expense.amount,
            'expreason':expense.expreason,
            'expby':expense.expby,
            'bankname':expense.bankname,
            'chequeordd':expense.chequeordd,
            'dateinbank':expense.dateinbank
        }
        return render(request,self.template_name,context)

    def post(self,request,pk):
        expense = get_object_or_404(Expense,pk=pk)
        data = request.POST
        expense.expname = data['expname']
        expense.expdate = data['expdate']
        expense.expmode = data['expmode']
        expense.amount = data['amount']
        expense.expreason = data['expreason']
        expense.expby = data['expby']
        expense.bankname = data['bankname']
        expense.chequeordd = data['chequeordd']
        expense.dateinbank = data['dateinbank']
        expense.detail = data['detail']
        expense.save()
        return redirect('expense')
        return render(request,self.template_name) 

class AddEmployeView(View,LoginRequiredMixin):
    template_name = 'addemploye.html'
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        data = request.POST
        employe = Employee()
        employe.empid = data['empid']
        employe.empname =data['empname']
        employe.desination = data['desination']
        employe.desginkdda = data['desginkdda']
        employe.phone = data['phone']
        employe.address = data['address']
        employe.save()
        return redirect("employee")
        return render(request,self.template_name)

class EmployeeView(View):
    template_name ="employee-detail.html"
    def get(self,request):
        employees = Employee.objects.all()
        tota = 0
        for employee in employees:
            tota += employee.empid
        context = {
            "employees":employees
        }
        return render(request,self.template_name ,context)

class EmployeeUpdateView(View):
    template_name = "update-employee.html"
    def get(self,request,pk):
        employee = get_object_or_404(Employee,pk=pk)
        context = {
            'empname':employee.empname,
            'desination':employee.desination,
            'desginkdda':employee.desginkdda,
            'phone':employee.phone,
            'address':employee.address
        }
        return render(request,self.template_name,context)

    def post(self,request,pk):
        employee = get_object_or_404(Employee,pk=pk)
        data = request.POST
        employee.empname = data['empname']
        employee.desination = data['desination']
        employee.desginkdda = data['desginkdda']
        employee.phone = data['phone']
        employee.address = data['address']
        employee.save()
        return redirect('employee')
        return render(request,self.template_name)

class EmployeeDeleteView(View):
    def get(self,request,pk):
        employe = Employee.objects.get(pk=pk)
        employe.delete()
        return redirect('employee')

def report(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()

    tot = 0
    for income in incomes:
        tot += income.incamt

    extot = 0
    for expense in expenses:
        extot += expense.amount

    travel = Expense.objects.filter(expname='Travel').aggregate(Sum('amount')) 
    meeting = Expense.objects.filter(expname='Meeting').aggregate(Sum('amount'))
    auditfees = Expense.objects.filter(expname='Audit Fees').aggregate(Sum('amount'))
    bankcharges = Expense.objects.filter(expname='Bankcharges').aggregate(Sum('amount'))
    servicecharges = Expense.objects.filter(expname='Servicecharges').aggregate(Sum('amount'))
    general = Expense.objects.filter(expname='General').aggregate(Sum('amount'))
    printing = Expense.objects.filter(expname='Printing').aggregate(Sum('amount'))
    bill = Expense.objects.filter(expname='Bill').aggregate(Sum('amount'))
    cashinhand = Expense.objects.filter(expname='Cash in Hand').aggregate(Sum('amount'))
    cashatbank = Expense.objects.filter(expname='Cash at Bank').aggregate(Sum('amount'))
    donation = Income.objects.filter(incname='Donation').aggregate(Sum('incamt'))
    rent = Income.objects.filter(incname='Rent').aggregate(Sum('incamt'))
    intrest = Income.objects.filter(incname='Intrest Collected').aggregate(Sum('incamt'))

    context = {
        "allexpenses":[
            {"name":"Travel","amount":travel},
            {"name":"Meeting","amount":meeting},
            {"name":"Audit Fees","amount":auditfees},
            {"name":"Bankcharges","amount":bankcharges},
            {"name":"Servicecharges","amount":servicecharges},
            {"name":"General","amount":general},
            {"name":"Printing","amount":printing},
            {"name":"Bill","amount":bill},
            {"name":"Cash in Hand","amount":cashinhand},
            {"name":"Cash at Bank","amount":cashatbank},
        ],
        "allincomes":[
            {"name":"Donation","incamt":donation},
            {"name":"Rent","incamt":rent},
            {"name":"Intrest Collected","incamt":intrest},
        ],
        "tot":tot,
        "extot":extot
    }
    return render(request,'report.html',context)

def addexpensetype(request):
    return render(request,'add-expense-type.html')

def incometype(request):
    context = {
        'incometypes':IncomeType.objects.all()
    }
    return render(request,'income-type.html',context)

def expensetype(request):
    context = {
        'expensetypes':ExpenseType.objects.all()
    }
    return render(request,'expense-type.html',context)

def income_csv(request):
    incomes = Income.objects.all() 
    response = HttpResponse(content_type = 'text\csv')
    response['content-Disposition'] = 'attachement; filename="income.csv"'
    writer = csv.writer(response,delimiter=',')
    writer.writerow(['IncName','Incdate','Incmode','Incamt','Increason','Incby','BankName','Cheque(or)DD','Dateinbank'])
    for income in incomes:
        writer.writerow([income.incname,income.incdate,income.incmode,income.incamt,income.increason,income.incby,income.bankname,income.chequeordd,income.dateinbank])
    return response
    
def expense_csv(request):
    expenses = Expense.objects.all() 
    response = HttpResponse(content_type = 'text\csv')
    response['content-Disposition'] = 'attachement; filename="expense.csv"'
    writer = csv.writer(response,delimiter=',')
    writer.writerow(['Expname','Expdate','Expmode','Amount','Expreason','Expby','Detail','BankName','Cheque(or)dd','Dateinbank'])
    for expense in expenses:
        writer.writerow([expense.expname,expense.expdate,expense.expmode,expense.amount,expense.expreason,expense.expby,expense.detail,expense.bankname,expense.chequeordd,expense.dateinbank])
    return response

def settings(request):
    inc = Income.objects.filter(incdate__gte=datetime.date(2020,10,1),incdate__lte=datetime.date(2020,10,30)).all()
    context = {
        "incs":inc
    }
    return render(request,'settings.html',context)

def error(request):
    return render(request,'404.html')
from django.shortcuts import render,redirect,get_object_or_404
from .models import(
    Expense,
    Income,
    IncomeType,
    ExpenseType,
    Employee,
    Transaction,
    Opening
)
from django.views.generic import View
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import FloatField
from django.contrib.auth import authenticate,forms
from django.http import Http404
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
class IncomeView(View):
    template_name = "income.html"
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            incomes = Income.objects.all()
            total = 0
            for income in incomes:
                total += income.incamt

            context = { 
                "incomes":incomes,
                "total":total
            }
            return render(request,self.template_name ,context)
        else:
            return redirect("error")

# expense view
class ExpenseView(View):
    template_name ="expense.html"
    def get(self,request):
        if request.user.is_authenticated:
            expenses = Expense.objects.all()

            context = {
                "expenses":expenses
            }   
            return render(request,self.template_name ,context)
        else:
            return redirect("error")

class AddincomeView(LoginRequiredMixin,View):
    template_name = 'addincome.html'
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request,incomemode):
        context={
            'incomemode':incomemode
        }
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
        return redirect("expense")
        return render(request,self.template_name)

class AddIncomeTypeView(LoginRequiredMixin,View):
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
        return redirect("income-type")
        return render(request,self.template_name)

class AddExpenseTypeView(LoginRequiredMixin,View):
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
        return redirect("expense-type")
        return render(request,self.template_name)

class ExpenseDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        expense = Expense.objects.get(pk=pk)
        expense.delete()
        return redirect("expense")

class IncomeDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        income = Income.objects.get(pk=pk)
        income.delete()
        return redirect("income")

class IncomeUpdateView(LoginRequiredMixin,View):
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

class ExpenseUpdateView(LoginRequiredMixin,View):
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

class AddEmployeView(LoginRequiredMixin,View):
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
        if request.user.is_authenticated:
            employees = Employee.objects.all()
            tota = 0
            for employee in employees:
                tota += employee.empid
            context = {
                "employees":employees
            }
            return render(request,self.template_name ,context)
        else:
            return redirect("error")

class EmployeeUpdateView(LoginRequiredMixin,View):
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

class EmployeeDeleteView(LoginRequiredMixin,View):
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request,pk):
        employe = Employee.objects.get(pk=pk)
        employe.delete()
        return redirect('employee')

class AddtransactionView(View):
    template_name = 'add-transaction.html'
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,self.template_name)
        else:
            return redirect("error")
    def post(self,request):
        data = request.POST
        transaction = Transaction()
        transaction.bankname = data['bankname']
        transaction.mode =data['mode']
        transaction.account_head = data['account_head']
        transaction.amt = data['amt']
        transaction.save()
        return redirect("transaction")
        return render(request,self.template_name)

class TransactionView(View):
    template_name ="transaction-details.html"
    def get(self,request):
        if request.user.is_authenticated:
            transactions = Transaction.objects.all()
            context = {
                "transactions":transactions
            }
            return render(request,self.template_name ,context)
        else:
            return redirect("error")

class TransactionDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        transaction = Transaction.objects.get(pk=pk)
        transaction.delete()
        return redirect('transaction')

class AddOpeningView(LoginRequiredMixin,View):
    template_name = 'starting.html'
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        data = request.POST
        opening = Opening()
        opening.cashinhand = data['cashinhand']
        opening.cashatbank = data['cashatbank']
        opening.cashatbankexp = data['cashatbankexp']
        opening.save()
        return redirect('open-details')
        return render(request,self.template_name)
     

class OpeningView(LoginRequiredMixin,View):
    template_name ="starting-details.html"
    def get(self,request):
        openings = Opening.objects.all()
        context = {
            "openings":openings
        }
        return render(request,self.template_name ,context)

class OpeningDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        opening = Opening.objects.get(pk=pk)
        opening.delete()
        return redirect('open-details')

class OpeningUpdateView(LoginRequiredMixin,View):
    template_name = 'opening-update.html'
    def get(self,request,pk):
        opening = get_object_or_404(Opening,pk=pk)
        context = {
            'cashinhand':opening.cashinhand,
            'cashatbank':opening.cashatbank,
            'cashatbankexp':opening.cashatbankexp
        }
        return render(request,self.template_name,context)
    def post(self,request,pk):
        opening = get_object_or_404(Opening,pk=pk)
        data = request.POST
        opening.cashinhand = data['cashinhand']
        opening.cashatbank = data['cashatbank']
        opening.cashatbankexp = data['cashatbankexp']
        opening.save()
        return redirect('open-details')
        return render(request,self.template_name)

def report(request):
    if request.user.is_authenticated:
        incomes = Income.objects.all()
        expenses = Expense.objects.all()
        openings = Opening.objects.all()

        tot = 0
        for income in incomes:
            tot += income.incamt

        amt = 0
        for opening in openings:
            amt = opening.cashinhand + opening.cashatbank
            #x = tot+opening.cashatbank
            
        fin = amt+tot
        '''
        extot = 0
        for expense in expenses:
            extot += expense.amount
            y = x-extot
         
        cih = fin-(extot+y)
        
        finexp =  cih+y+extot
        '''
        extot = 0
        a=0
        for expense in expenses:
            extot += expense.amount
            a=fin-extot

        for opening in openings:
            b=a-opening.cashatbankexp

        finexp = extot+a

        travel = Expense.objects.filter(expname='Travel').aggregate(Sum('amount')) 
        meeting = Expense.objects.filter(expname='Meeting').aggregate(Sum('amount'))
        auditfees = Expense.objects.filter(expname='Audit Fees').aggregate(Sum('amount'))
        bankcharges = Expense.objects.filter(expname='Bankcharges').aggregate(Sum('amount'))
        servicecharges = Expense.objects.filter(expname='Servicecharges').aggregate(Sum('amount'))
        general = Expense.objects.filter(expname='General').aggregate(Sum('amount'))
        printing = Expense.objects.filter(expname='Printing').aggregate(Sum('amount'))
        bill = Expense.objects.filter(expname='Bill').aggregate(Sum('amount'))
        donation = Income.objects.filter(incname='Donation').aggregate(Sum('incamt'))
        rent = Income.objects.filter(incname='Rent').aggregate(Sum('incamt'))
        intrest = Income.objects.filter(incname='Intrest Collected').aggregate(Sum('incamt'))
        sports = Income.objects.filter(incname='Sports Loan').aggregate(Sum('incamt'))
        loan = Income.objects.filter(incname='Loan Recived').aggregate(Sum('incamt'))
        subscription = Income.objects.filter(incname='Subscription Fees').aggregate(Sum('incamt'))
        entry = Income.objects.filter(incname='Entry Fees').aggregate(Sum('incamt'))
        addvertisment = Income.objects.filter(incname='Addvertisment').aggregate(Sum('incamt'))
        commission = Income.objects.filter(incname='Commission Earned').aggregate(Sum('incamt'))
        comman = Income.objects.filter(incname='General Income').aggregate(Sum('incamt'))

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
            ],
            "allincomes":[
                {"name":"Donation","incamt":donation},
                {"name":"Rent","incamt":rent},
                {"name":"Intrest Collected","incamt":intrest},
                {"name":"Sports Loan","incamt":sports},
                {"name":"Loan Recived","incamt":loan},
                {"name":"Subscription Fees","incamt":subscription},
                {"name":"Entry Fees","incamt":entry},
                {"name":"Addvertisment","incamt":addvertisment},
                {"name":"Commission Earned","incamt":commission},
                {"name":"General Income","incamt":comman},
            ],
            "tot":tot,#all income tot
            "extot":extot,# all exp tot or closing balance
            "openings":openings,
            "fin":fin,# final income
            #"y":y, cash at bank
            #"cih":cih, cash in hand
            #"finexp":finexp final expense 
            "b":b,
            "finexp":finexp
        }
        return render(request,'report.html',context)
    else:
        return redirect("error")

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

def Incomefilter(request):
    inc = Income.objects.filter(incdate__gte=datetime.date(2022,10,1),incdate__lte=datetime.date(2020,10,30)).all()
    con = {
        "incms":inc
    }
    if request.method == 'POST':
        maxi = request.POST.get('date_max').split('-')
        mini = request.POST.get('date_min').split('-')
        incm = Income.objects.filter(incdate__gte=datetime.date(int(mini[0]),int(mini[1]),int(mini[2])),incdate__lte=datetime.date(int(maxi[0]),int(maxi[1]),int(maxi[2]))).all()          
        con = {
            "incms":incm,
        }
    return render(request,'income-filter.html',con)

def Expensefilter(request):
    exp = Expense.objects.filter(expdate__gte=datetime.date(2022,10,1),expdate__lte=datetime.date(2020,10,30)).all()
    con = {
        "expms":exp
    }
    if request.method == 'POST':
        maxi = request.POST.get('date_max').split('-')
        mini = request.POST.get('date_min').split('-')
        expm = Expense.objects.filter(expdate__gte=datetime.date(int(mini[0]),int(mini[1]),int(mini[2])),expdate__lte=datetime.date(int(maxi[0]),int(maxi[1]),int(maxi[2]))).all()          
        con = {
            "expms":expm,
        }
    return render(request,'expense-filter.html',con)

def error(request):
    return render(request,'404error.html')

def voucher(request):
    return render(request,'voucher.html')

#cih = cash in hand 
#y = cash at bank
# extot = closing blanace
# tot = all income total
# to find Total 

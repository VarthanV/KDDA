from django.urls import path
from . import views
from .views import (
    ExpenseView,
    IncomeView,
    AddincomeView,
    AddexpenseView,
    AddIncomeTypeView,
    ExpenseDeleteView,
    IncomeDeleteView,
    IncomeUpdateView,
    ExpenseUpdateView,
    AddExpenseTypeView,
    AddEmployeView,
    EmployeeView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    TransactionView,
    AddtransactionView,
    TransactionDeleteView,
    AddOpeningView,
    OpeningView,
    OpeningDeleteView,
    OpeningUpdateView
)

urlpatterns = [
    path('',views.home,name='home'),
    path('details/',views.details,name='details'),

    path('income/',views.IncomeView.as_view(),name="income"),   
    path('expense/',views.ExpenseView.as_view(),name="expense"),
    path('employee/',views.EmployeeView.as_view(),name="employee"),
    path('opening/',views.AddOpeningView.as_view(),name="opening"),
    path('open-details/',views.OpeningView.as_view(),name='open-details'),
    path('transaction/',views.TransactionView.as_view(),name="transaction"),

    path('add-income/<str:incomemode>/',views.AddincomeView.as_view(),name ='add-income'),
    path('add-employe/',views.AddEmployeView.as_view(),name ='add-employe'),
    path('add-expense/<str:expensemode>/',views.AddexpenseView.as_view(),name ='add-expense'),
    path('add-transaction/',views.AddtransactionView.as_view(),name ='add-transaction'),

    path('add-income-type/',views.AddIncomeTypeView.as_view(),name ='add-income-type'),
    path('add-expense-type/',views.AddExpenseTypeView.as_view(),name='add-expense-type'),

    path('income-type/',views.incometype,name='income-type'),
    path('expense-type/',views.expensetype,name='expense-type'),

    path("delete/expense/<str:pk>/",views.ExpenseDeleteView.as_view(),name='delete-expense'),
    path("delete/income/<str:pk>/",views.IncomeDeleteView.as_view(),name='delete-income'),
    path("delete/employee/<str:pk>/",views.EmployeeDeleteView.as_view(),name='delete-employe'),
    path("delete/transaction/<str:pk>/",views.TransactionDeleteView.as_view(),name='delete-transaction'),
    path("delete/opening/<str:pk>/",views.OpeningDeleteView.as_view(),name='delete-opening'),

    path('income/<int:pk>/update/', views.IncomeUpdateView.as_view(), name='income-update'),
    path('expense/<int:pk>/update/', views.ExpenseUpdateView.as_view(), name='expense-update'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('opening/<int:pk>/update/', views.OpeningUpdateView.as_view(), name='opening-update'),

    path('report/',views.report,name="report"),

    path('income-csv/',views.income_csv,name='income-csv'),
    path('expense-csv/',views.expense_csv,name='expense-csv'),

    path('income-filter/',views.Incomefilter,name='income-filter'),
    path('expense-filter/',views.Expensefilter,name='expense-filter'),
]

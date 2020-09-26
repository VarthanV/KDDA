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
    EmployeeView
)

urlpatterns = [
    path('',views.home,name='home'),
    path('details/',views.details,name='details'),

    path('income/',views.IncomeView.as_view(),name="income"),   
    path('expense/',views.ExpenseView.as_view(),name="expense"),
    path('employee/',views.EmployeeView.as_view(),name="employee"),

    path('add-income/<str:incomemode>/',views.AddincomeView.as_view(),name ='add-income'),
    path('add-employe/',views.AddEmployeView.as_view(),name ='add-employe'),
    path('add-expense/<str:expensemode>/',views.AddexpenseView.as_view(),name ='add-expense'),

    path('add-income-type/',views.AddIncomeTypeView.as_view(),name ='add-income-type'),
    path('add-expense-type/',views.AddExpenseTypeView.as_view(),name='add-expense-type'),

    path('income-type/',views.incometype,name='income-type'),
    path('expense-type/',views.expensetype,name='expense-type'),

    path("delete/expense/<str:pk>/",views.ExpenseDeleteView.as_view(),name='delete-expense'),
    path("delete/income/<str:pk>/",views.IncomeDeleteView.as_view(),name='delete-income'),

    path('income/<int:pk>/update/', views.IncomeUpdateView.as_view(), name='income-update'),
    path('expense/<int:pk>/update/', views.ExpenseUpdateView.as_view(), name='expense-update'),

    path('report/',views.report,name="report"),
]

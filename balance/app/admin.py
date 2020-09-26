from django.contrib import admin
from .models import (
    Employee,
    Income,
    Expense,
    IncomeType,
    ExpenseType
)
# Register your models here.
admin.site.register(Employee)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(IncomeType)
admin.site.register(ExpenseType)
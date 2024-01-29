
# Register your models here.
# employees/admin.py
from django.contrib import admin
from .models import Employee,Department,EmployeeSalary,contact

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'designation', 'department', 'reporting_manager')

admin.site.register(Employee, EmployeeAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor')
    
admin.site.register(Department,DepartmentAdmin)


class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'start_date', 'end_date')

admin.site.register(EmployeeSalary,EmployeeSalaryAdmin)



class contactadmin(admin.ModelAdmin):
    list_display=('name','surname','phone','email','msg')

admin.site.register(contact,contactadmin)
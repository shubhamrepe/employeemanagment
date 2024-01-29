from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from .models import *
from .forms import DepartmentForm, EmployeeForm, SalaryEntryForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_l.html', {'employees': employees})


def employee_detail(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    return render(request, 'emp_d.html', {'employee': employee})


def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('emp_l')
    return render(request, 'delete_emp.html', {'employee': employee})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_l')
    else:
        form = EmployeeForm()
    return render(request, 'add_emp.html', {'form': form})



def department_list(request):
    department=Department.objects.all()
    data={'department':department}
    return render(request,'dept_list.html',data)


def department_detail(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    return render(request, 'dept_detail.html', {'department': department})


def delete_department(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    if request.method == 'POST':
        department.delete()
        return redirect('dept_detail')
    return render(request, 'delet_dept.html', {'department': department})


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dept_l')
    else:
        form = DepartmentForm()
    return render(request, 'add_dep.html', {'form': form, 'form_title': 'Add Department'})

def add_salary_entry(request):
    if request.method == 'POST':
        form = SalaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryEntryForm()
    return render(request, 'add_sal.html', {'form': form, 'form_title': 'Add Salary Entry'})


def salary_list(request):
    salary_entries = EmployeeSalary.objects.all()
    return render(request, 'salary_l.html', {'salary_entries': salary_entries})


def update_salary_entry(request, entry_id):
    salary_entry = get_object_or_404(EmployeeSalary, id=entry_id)
    if request.method == 'POST':
        form = SalaryEntryForm(request.POST, instance=salary_entry)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryEntryForm(instance=salary_entry)
    return render(request, 'update_salary.html', {'form': form, 'form_title': 'Update Salary Entry'})

def delete_salary(request, entry_id):
    salary = get_object_or_404(EmployeeSalary, id=entry_id)
    if request.method == 'POST':
        salary.delete()
        return redirect('salary_list')
    return render(request, 'delete_salary.html', {'salary': salary})



def contact_us(request):
    if request.method =="GET":
        return render(request,'contact_us.html')
    else:
      name=request.POST["name"]
      surname=request.POST["surname"]
      phone=request.POST["phone"]
      email=request.POST["email"]
      msg=request.POST["msg"]
      contact.objects.create(name=name,surname=surname,phone=phone,email=email,msg=msg)
      return redirect('/')
     
def update_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emp_l')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update_emp.html', {'form': form, 'employee': employee})



# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator

class Department(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('Associate', 'Associate'),
        ('TL', 'Team Lead'),
        ('Manager', 'Manager'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.salary} ({self.start_date} to {self.end_date})"
    
class contact(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    phone=models.BigIntegerField(default=2)
    email=models.EmailField(default="shubham10@gmail.com")
    msg=models.CharField(max_length=1000)


    def __str__(self):
        return f"{self.name}"

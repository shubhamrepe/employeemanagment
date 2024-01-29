from django.contrib import admin
from django.urls import path
from emp_app import views

urlpatterns = [
    path('',views.index,name="index"),

    path('add/',views. add_employee, name='add_employee'),
    path('list/',views. employee_list, name='emp_l'),
    path('dept_list/',views.department_list,name='dept_l'),
    path('add_dept/',views.add_department,name='add_department'),

    path('salaries/', views.salary_list, name='salary_list'),
    path('add_salary', views.add_salary_entry, name='add_salary_entry'),

    path('contact_us/',views. contact_us, name='contact_us'),


    path('<int:emp_id>/update/', views.update_employee, name='update_employee'),
    path('<int:emp_id>/delete/', views.delete_employee, name='delete_employee'),
    path('dept_details/<int:dept_id>',views.department_detail,name='department_detail'),
    path('delete_dept/<int:dept_id>/', views.delete_department, name='delete_dept'),

    path('add_salary', views.add_salary_entry, name='add_salary_entry'),
    path('delete_salary/<int:entry_id>/', views.delete_salary, name='delete_salary'),
    path('salary/edit/<int:entry_id>/', views.update_salary_entry, name='update_salary_entry'),

]
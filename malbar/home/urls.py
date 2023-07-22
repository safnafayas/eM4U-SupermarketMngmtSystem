from django.contrib.auth import views as auth_view
from django.urls import reverse
from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from home import views as home_views
from django.conf import settings

# from django.urls import reverse
# from django.core.urlresolvers import reverse

urlpatterns = [

    path('', views.index, name='index'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),

    path('employeelogin/', views.employeelogin, name='employeelogin'),
    path('deleteemployee/<int:pk>', views.deleteemployee, name='deleteemployee'),
    path('updateemployee/<int:pk>',
         views.updateemployee.as_view(), name='updateemployee'),
    path('deletetaskassign/<int:pk>',
         views.deletetaskassign, name='deletetaskassign'),
    path('updatetaskassign/<int:pk>',
         views.updatetaskassign.as_view(), name='updatetaskassign'),
    path('mgremployeedetails/', views.mgremployeedetails,
         name='mgremployeedetails'),
    path('deletetodoloist/<int:pk>',
         views.deletetodolist, name='deletetodolist'),
    path('updatetodolist/<int:pk>',
         views.updatetodolist.as_view(), name='updatetodolist'),



    path('addemployee/', views.addemployee, name='addemployee'),

    path('customerreviewform/', views.customerreviewform,
         name='customerreviewform'),






    #     path('', home_views.index, name='index'),
    path('Addemployee/', views.Addemployee, name='Addemployee'),
    path('mgrlogin/', views.login, name='mgrlogin'),
    path('alerts/', views.alerts, name='alerts'),
    path('deletealert/<int:pk>',
         views.deletealert, name='deletealert'),
    path('updatealert/<int:pk>',
         views.updatealert.as_view(), name='updatealert'),
    path('mgrallstockreports/', views.mgrallstockreports,
         name='mgrallstockreports'),
    path('mgrallsalesreports/', views.mgrallsalesreports,
         name='mgrallsalesreports'),
    path('deletesalesreport/<int:pk>',
         views.deletesalesreport, name='deletesalesreport'),
    path('updatesalesreport/<int:pk>',
         views.updatesalesreport.as_view(), name='updatesalesreport'),
    path('deletestockreport/<int:pk>',
         views.deletestockreport, name='deletestockreport'),
    path('updatestockreport/<int:pk>',
         views.updatestockreport.as_view(), name='updatestockreport'),

    path('Sales_Report_form/', views.Sales_Report_form, name='Sales_Report_form'),
    path('stock_report_form/', views.stock_report_form, name='stock_report_form'),
    path('taskassignment/', views.taskassignment, name='taskassignment'),
    path('todolist/', views.Todolist, name='todolist'),
    path('manager_register/', views.manager_register, name='managersignup'),
    path('employee_register/', views.employee_register, name='employeesignup'),
    path('Home/', views.Home, name='Home'),
    path('alertstaff/', views.alertstaff, name='alertstaff'),
    path('rate/<int:post_id>/<int:rating>/', views.rate),
    path('customerfeedback/', views.customerfeedback,),

]

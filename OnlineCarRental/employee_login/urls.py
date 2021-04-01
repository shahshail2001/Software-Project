from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('adminlogin/', views.adminlogin),
    url('adminsignup/', views.adminsignup),
    url('getemployee/', views.getemployee),
    url('success/', views.success),
    url('adminhomepage/', views.adminhomepage),
    url('deleteemployeeinfo/', views.deleteemployeeinfo),
    url('deleteemployee/', views.deleteemployee),
    url('employeedeleteunsuccessful/', views.employeedeleteunsuccessful),
    url('getemployeesinfo/', views.getemployeesinfo),
    url('employee/', views.EmployeeListView.as_view(), name='employee'),
    url('addemployeeinfo/', views.addemployeeinfo),
]

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('getcustomer/', views.getcustomer),
    url('customerinfo/', views.customerinfo),
    url('signout/', views.signout),
    url('registersuccess/', views.registersuccess),
    url('deletecustomer/', views.deletecustomer),
    url('delete_customer/', views.delete_customer),
    url('viewcustomer/', views.viewcustomer),
    url('customerlogin/', views.customerlogin),
    url('customerloginpage/', views.customerloginpage),
    url('customer/', views.CustomerListView.as_view(), name='customer')
]

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('getcustomer/', views.getcustomer),
    url('customerinfo/', views.customerinfo),
    url('registersuccess/', views.registersuccess),
    url('deletecustomer/', views.deletecustomer),
    url('delete_customer/', views.delete_customer),
    url('customer/', views.CustomerListView.as_view(), name='customer')
]

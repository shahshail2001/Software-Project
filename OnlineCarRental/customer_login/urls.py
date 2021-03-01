from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('getcustomer/', views.getcustomer),
    url('customerinfo/', views.customerinfo),
    url('registersuccess/', views.registersuccess),
    url('customer/', views.CustomerListView.as_view(), name='customer')
]

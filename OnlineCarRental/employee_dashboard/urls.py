from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('addcarinfo/', views.addcarinfo),
    url('getcarinfo/', views.getcarinfo),
    url('addsuccess/', views.addsuccess),
    url('car/', views.CarListView.as_view(), name='car')
]
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('login/', views.login),
    url('authorize/', views.authorize),
    url('update_car/', views.update_car()),
    url('addcarinfo/', views.addcarinfo),
    url('getcarinfo/', views.getcarinfo),
    url('addsuccess/', views.addsuccess),
    url('car/', views.CarListView.as_view(), name='car'),
    url('getcars/', views.getcars),
    url('deleteinfo/', views.deleteinfo),
    url('deletecarinfo/', views.deletecarinfo),
    url('deleteunsuccessful/', views.deleteunsuccessful),
    url('back_to_homepage/', views.back_to_homepage),
    url('logout/', views.logout),
]

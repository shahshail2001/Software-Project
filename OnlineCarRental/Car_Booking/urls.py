from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('BookCar', views.BookCar),
    url('booking', views.booking),
    url('book', views.book)
]

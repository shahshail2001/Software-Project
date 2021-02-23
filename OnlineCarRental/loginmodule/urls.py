from django.urls import path
from loginmodule.views import login, auth_view, logout, loggedin, invalidlogin
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', login),
    path('/auth/', auth_view),
    path('/logout/', logout),
    path('/loggedin/', loggedin),
    path('/invalidlogin/', invalidlogin),
]

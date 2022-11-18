from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('userregistration/', views.userRegistration, name = 'userregister'),
    path('adminregistration/', views.adminRegistration, name = 'adminregister'),
    path('signin/', views.signin, name = 'signin'),
    path('signout', views.signout, name = 'signout'),
    path('otp/', views.otp, name = 'otp'),

]    
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index), 
    path('index/', views.index, name='index'), 
    path('navbar/', views.navbar, name='navbar'), 
    path('footer/', views.footer, name='footer'), 
    path('about/', views.about, name='about'), 
    path('service/', views.service, name='service'), 
    path('enterprise_services/', views.enterprise_services, name='enterprise_services'), 
    path('standard_services/', views.standard_services, name='standard_services'),
   
    path('contact/', views.contact, name='contact'),  

]
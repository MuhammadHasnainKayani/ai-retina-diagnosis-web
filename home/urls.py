
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.contact, name='contact'),
    
    path('contact',views.contact,name='contact'),
   
    path('land',views.contact,name='contact'),
    
]

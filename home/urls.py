from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
  path("",views.index,name='home'),
  path("judge",views.judge,name='judge'), 
  path("partyname",views.partyname,name='partyname'),  
]
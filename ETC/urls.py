from django.urls import path
from django.urls import path
from .import views
from django.contrib import admin

urlpatterns =[
    path('',views.index,name='index'),
    path('check',views.check,name='check')


]
#path('abc',views.abc,name='abc')
from django.contrib import admin
from django.urls import path,include;
from myapp import views;

#from myapp import urls;
urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.add,name="add"),
    path('change/<item_id>/',views.change,name="change"),
    path('del/',views.delcom,name="del"),
    path('delall',views.delall,name="delall"),
];

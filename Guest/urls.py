from django.contrib import admin
from django.urls import path,include
from Guest import views

app_name="wguest"

urlpatterns = [
    
    path('UserRegistration/', views.UserRegister,name="UserRegister"),
    path('ajax_place/', views.ajax_place,name="ajax_place"),
    path('ShopRegistration/', views.ShopRegister,name="ShopRegister"),
    path('Userlogin/',views.Userlogin,name="Userlogin"),
    path('GuestHome/',views.GuestHome,name="GuestHome"),
]

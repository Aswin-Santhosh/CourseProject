from django.contrib import admin
from django.urls import path
from Basics import views

urlpatterns = [
    
    path('Calculator/', views.Calculation,name="Calculation"),
    path('Circle/', views.circlearea,name="circlearea"),
    path('Largestof3/', views.Largest,name="Largest"),
    path('Paliandrome/', views.Reverse,name="Reverse"),
    path('Palinbtwn2limit/', views.Limits,name="Limits"),
    path('RankList/', views.Student,name="Student"),
    path('Employee/', views.Salary,name="Salary"),
    path('Collegehome/', views.Collegehome,name="Collegehome"),
]

from django.contrib import admin
from django.urls import path,include
from User import views

app_name="wuser"

urlpatterns = [
    
    path('Userhome/', views.Userhome,name="Userhome"),
    path('MyProfile/', views.MyProfile,name="MyProfile"),
    path('Editprofile/', views.Editprofile,name="Editprofile"),
    path('ChangePass/', views.ChangePass,name="ChangePass"),
    path('ProductDetail/',views.ProductDetail,name="ProductDetail"),
    path('Ajax_Product/',views.Ajax_Product,name="Ajax_Product"),
    path('ajax_subcategory/',views.ajax_subcategory,name="ajax_subcategory"),
    
    path('ProductGallery<int:pid>/',views.ProductGallery,name="ProductGallery"),
    path('Productbooking<int:pid>/',views.Productbooking,name="Productbooking"),
    path('Bookedproduct/',views.Bookedproduct,name="Bookedproduct"),
    path('Complaint/',views.Complaint,name="Complaint"),   
    path('Feedback/',views.Feedback,name="Feedback"),   
]
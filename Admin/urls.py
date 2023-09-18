from django.contrib import admin
from django.urls import path,include
from Admin import views

app_name="wadmin"

urlpatterns = [
    path('Adminhome/', views.Adminhome,name="Adminhome"),
    path('District/', views.Location,name="Location"),
    path('Place/', views.Placelocation,name="Placelocation"),
    path('Category/', views.Categorys,name="Categorys"),
    path('SubCategory/', views.Subcategorys,name="Subcategorys"),
    path('AdminRegistration/', views.Registration,name="Registration"),
    path('UserDetails/', views.Userdetails,name="Userdetails"),
    path('ShopDetails/', views.Shopdetails,name="Shopdetails"),
    path('ComplaintDetails/', views.ComplaintDetails,name="ComplaintDetails"),
    path('reply_complaint/<int:rid>',views.reply_complaint,name="reply_complaint"),
    path('FeedbackDetail/', views.FeedbackDetail,name="FeedbackDetail"),
    path('ProductType/', views.ProductType,name="ProductType"),

    path('del_district/<int:did>',views.del_district,name="del_district"),
    path('del_place/<int:did>',views.del_place,name="del_place"),
    path('del_category/<int:did>',views.del_category,name="del_category"),
    path('del_subcategory/<int:did>',views.del_subcategory,name="del_subcategory"),
    path('del_admin/<int:did>',views.del_admin,name="del_admin"),
    path('del_productType/<int:did>',views.del_productType,name="del_productType"),
        
]

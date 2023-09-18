from django.contrib import admin
from django.urls import path,include
from Shop import views

app_name="wshop"

urlpatterns = [

    path('ShopHome/', views.ShopHome,name="ShopHome"),
    path('Myprofile/', views.Myprofile,name="Myprofile"),
    path('editprofile/', views.editprofile,name="editprofile"),
    path('ChangePass/', views.ChangePass,name="ChangePass"),
    path('Product/', views.Product,name="Product"),
    path('ProductDetail/', views.ProductDetail,name="ProductDetail"),
    path('ajax_subcategory/', views.ajax_subcategory,name="ajax_subcategory"),
    path('del_product/<int:did>', views.del_product,name="del_product"),
    path('Gallery/<int:pid>', views.Gallery,name="Gallery"),
    path('BookedProduct/',views.BookedProduct,name="BookedProduct"),
    path('OrderAccept/<int:aid>', views.OrderAccept,name="OrderAccept"),
    path('OrderReject/<int:rid>', views.OrderReject,name="OrderReject"),
    path('AcceptedOrder/',views.AcceptedOrder,name="AcceptedOrder"),
    path('RejectedOrder/',views.RejectedOrder,name="RejectedOrder"),
    path('Complaint/',views.Complaint,name="Complaint"),
]
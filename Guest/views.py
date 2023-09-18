from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *

# Create your views here.

def GuestHome(request):
    return render(request,"Guest/GuestHome.html")




def UserRegister(request):
    disdata=tbl_district.objects.all()
    placdata=tbl_place.objects.all()
    userdata=tbl_userregister.objects.all()
    if request.method=="POST" and request.FILES:
        plcid=tbl_place.objects.get(id=request.POST.get('ddlplace'))
        tbl_userregister.objects.create(user_name=request.POST.get('txtname'),
                                        user_contact=request.POST.get('txtcontact'),
                                        user_email=request.POST.get('txtemail'),
                                        user_gender=request.POST.get('radio'),
                                        user_address=request.POST.get('txtaddress'),
                                        user_password=request.POST.get('txtpassword'),
                                        user_photo=request.FILES.get('filephoto'),place=plcid)
        return render(request,"Guest/UserRegistration.html",{'DIS':disdata,'USER':userdata})
    else:
        return render(request,"Guest/UserRegistration.html",{'DIS':disdata,'USER':userdata})
    

def ShopRegister(request):
    disdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST" and request.FILES:
        plcid=tbl_place.objects.get(id=request.POST.get('ddlplace'))
        tbl_shopregistration.objects.create(shop_name=request.POST.get('txtshopname'),
                                            owner_name=request.POST.get('txtowner'),
                                            shop_contact=request.POST.get('txtcontact'),
                                            shop_email=request.POST.get('txtemail'),
                                            shop_address=request.POST.get('txtaddress'),
                                            shop_logo=request.FILES.get('filelogo'),
                                            shop_proof=request.FILES.get('fileproof'),
                                            shop_since=request.POST.get('txtsince'),
                                            shop_password=request.POST.get('txtpassword'),
                                            place=plcid)
        return render(request,"Guest/ShopRegistration.html",{'DIS':disdata})
    else:
        return render(request,"Guest/ShopRegistration.html",{'DIS':disdata})


#user Login

def Userlogin(request):
    if request.method=="POST":
        Email=request.POST.get('email')
        Pass=request.POST.get('password')
        adminlog=tbl_adminregister.objects.filter(admin_email=Email,admin_password=Pass).count()
        userlog=tbl_userregister.objects.filter(user_email=Email,user_password=Pass).count()
        shoplog=tbl_shopregistration.objects.filter(shop_email=Email,shop_password=Pass).count()
        if userlog > 0:
            user=tbl_userregister.objects.get(user_email=Email,user_password=Pass)
            request.session['uid']=user.id
            request.session['upassword']=user.user_password
            return redirect('wuser:Userhome')
        elif adminlog > 0:
            admin=tbl_adminregister.objects.get(admin_email=Email,admin_password=Pass)
            request.session['aid']=admin.id
            return redirect('wadmin:Adminhome')
        elif shoplog > 0:
            shop=tbl_shopregistration.objects.get(shop_email=Email,shop_password=Pass)
            request.session['sid']=shop.id
            return redirect('wshop:ShopHome')
        else:
            return render(request,"Guest/Login.html",{'msg':"Invalid Credentials!!"})
    else:
        return render(request,"Guest/Login.html")
   




def ajax_place(request):
    dist=tbl_district.objects.get(id=request.GET.get('DIST'))
    plc=tbl_place.objects.filter(district=dist)
    return render(request,"Guest/AjaxPlace.html",{'PLC':plc})
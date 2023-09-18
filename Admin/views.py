from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
# Create your views here.



def Adminhome(request):
    if 'aid' in request.session:
        return render(request,"Admin/AdminHome.html")
    else:
        return redirect("wguest:Userlogin")

#district And Place

def Location(request):
    if 'aid' in request.session:
        disdata=tbl_district.objects.all()
        if request.method=="POST":
            tbl_district.objects.create(district_name=request.POST.get('txtdistrict'))
            return render(request,"Admin/District.html",{'Data':disdata})
        else:
            return render(request,"Admin/District.html",{'Data':disdata})
    else:
        return redirect("wguest:Userlogin")
def Placelocation(request):
    if 'aid' in request.session:
        disdata=tbl_district.objects.all()
        plcdata=tbl_place.objects.all()
        if request.method=="POST":
            disid=tbl_district.objects.get(id=request.POST.get('ddldistrict'))
            tbl_place.objects.create(place_name=request.POST.get('txtplace'),
                                    place_pin=request.POST.get('txtpin'),district=disid)
            return render(request,"Admin/Place.html",{'Data':plcdata,'DIS':disdata})
        else:
            return render(request,"Admin/Place.html",{'Data':plcdata,'DIS':disdata})
    else:
        return redirect("wguest:Userlogin")

# Category And Sub Category

def Categorys(request):
    if 'aid' in request.session:
        catedata=tbl_category.objects.all()
        if request.method=="POST":
            tbl_category.objects.create(category_name=request.POST.get('txtcategory'))
            return render(request,"Admin/Category.html",{'data':catedata})
        else:
            return render(request,"Admin/Category.html",{'data':catedata})
    else:
        return redirect("wguest:Userlogin")

def ProductType(request):
    if 'aid' in request.session:
        typedata=tbl_product_type.objects.all()
        if request.method=="POST":
            tbl_product_type.objects.create(product_type=request.POST.get('txtproducttype'))
            return render(request,"Admin/ProductType.html",{'data':typedata})
        else:
            return render(request,"Admin/ProductType.html",{'data':typedata})
    else:
        return redirect("wguest:Userlogin")



def Subcategorys(request):
    if 'aid' in request.session:
        catedata=tbl_category.objects.all()
        subdata=tbl_subcategory.objects.all()
        if request.method=="POST":
            cateid=tbl_category.objects.get(id=request.POST.get('ddlcategory'))
            tbl_subcategory.objects.create(subcategory_name=request.POST.get('txtsubcategory'),category=cateid)
            return render(request,"Admin/SubCategory.html",{'data':subdata,'CATE':catedata})
        else:
            return render(request,"Admin/SubCategory.html",{'data':subdata,'CATE':catedata})
    else:
        return redirect("wguest:Userlogin")    

#Admin Registration

def Registration(request):
    if 'aid' in request.session:
        admindata=tbl_adminregister.objects.all()
        if request.method=="POST":
            tbl_adminregister.objects.create(admin_name=request.POST.get('txtadminname'),
                                            admin_contact=request.POST.get('txtcontact'),
                                            admin_email=request.POST.get('txtadminemail'),
                                            admin_password=request.POST.get('txtpassword'))
            return render(request,"Admin/AdminRegistration.html",{'addata':admindata})
        else:
            return render(request,"Admin/AdminRegistration.html",{'addata':admindata})
    else:
        return redirect("wguest:Userlogin")    


# user Details
def Userdetails(request):
    if 'aid' in request.session:
        userdata=tbl_userregister.objects.all()
        return render(request,"Admin/UserDetails.html",{'USER':userdata})
    else:
        return redirect("wguest:Userlogin")    

#shop Details
def Shopdetails(request):
    if 'aid' in request.session:
        shopdata=tbl_shopregistration.objects.all()
        return render(request,"Admin/ShopDetails.html",{'SHOP':shopdata})
    else:
        return redirect("wguest:Userlogin")    


def ComplaintDetails(request):
    if 'aid' in request.session:
        userdata=tbl_userregister.objects.all()
        shopdata=tbl_shopregistration.objects.all()
        complaint=tbl_complaint.objects.filter(user__in=userdata)
        scomplaint=tbl_complaint.objects.filter(shop__in=shopdata)
        return render(request,"Admin/ComplaintDetails.html",{'DATA':complaint,'SHOPDATA':scomplaint})
    else:
        return redirect("wguest:Userlogin")    

def reply_complaint(request,rid):
    if 'aid' in request.session:
        data=tbl_complaint.objects.get(id=rid)
        if request.method=='POST':
            data.complaint_reply=request.POST.get('complaintreply')
            data.complaint_status=1
            data.save()
            return redirect('wadmin:ComplaintDetails')
        else:
            return render(request,"Admin/ComplaintReply.html",{'DATA':data})
    else:
        return redirect("wguest:Userlogin")    


def FeedbackDetail(request):
    if 'aid' in request.session:
        feedback=tbl_feedback.objects.all()
        return render(request,"Admin/FeedbackDetails.html",{'DATA':feedback})
    else:
        return redirect("wguest:Userlogin")    
        


#-----delete-----#

def del_district(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('wadmin:Location')

def del_place(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('wadmin:Placelocation')


def del_category(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect('wadmin:Categorys')

def del_productType(request,did):
    tbl_product_type.objects.get(id=did).delete()
    return redirect('wadmin:ProductType')

def del_subcategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect('wadmin:Subcategorys')

def del_admin(request,did):
    tbl_adminregister.objects.get(id=did).delete()
    return redirect('wadmin:Registration')
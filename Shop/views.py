from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Shop.models import *
from User.models import *


# Create your views here.

def ShopHome(request):
    if 'sid' in request.session:
        data=tbl_shopregistration.objects.get(id=request.session['sid'])
        return render(request,"Shop/ShopHome.html",{'Data':data})
    else:
        return redirect("wguest:Userlogin")    
        

#my Profile

def Myprofile(request):
    if 'sid' in request.session:
        data=tbl_shopregistration.objects.get(id=request.session['sid'])
        return render(request,"Shop/Myprofile.html",{'Data':data})
    else:
        return redirect("wguest:Userlogin")    
 

def editprofile(request):
    if 'sid' in request.session:
        data=tbl_shopregistration.objects.get(id=request.session['sid'])
        if request.method=="POST":
            data.owner_name=request.POST.get('txtname')
            data.shop_contact=request.POST.get('txtcontact')
            data.shop_email=request.POST.get('txtemail')
            data.shop_address=request.POST.get('txtaddress')
            data.save()
            return redirect('wshop:Myprofile')
        else:
            return render(request,"Shop/EditProfile.html",{'Data':data})
    else:
        return redirect("wguest:Userlogin")    
        
    
# Change Password
def ChangePass(request):
    if 'sid' in request.session:
        data=tbl_shopregistration.objects.get(id=request.session['sid'])
        password=data.shop_password
        if request.method=="POST":
            currentpass=request.POST.get('txtcurrentpass')
            if currentpass==password:
                newpass=request.POST.get('txtnewpass')
                confrimpass=request.POST.get('txtcomnfirmpass')
                if newpass==confrimpass:
                    data.shop_password=request.POST.get('txtnewpass')
                    data.save()
                    return redirect('wshop:Myprofile')
            else:
                return render(request,"Shop/ChangePassword.html",{'msg':"Invalid Credentials!!"})
        else:
            return render(request,"Shop/ChangePassword.html")
    else:
        return redirect("wguest:Userlogin")    
 



#Product adding

def Product(request):
    if 'sid' in request.session:
        typedata=tbl_product_type.objects.all()
        catedata=tbl_category.objects.all()
        shopid=tbl_shopregistration.objects.get(id=request.session['sid'])
        if request.method=="POST" and request.FILES:
            typeid=tbl_product_type.objects.get(id=request.POST.get('ddlproducttype'))
            subcateid=tbl_subcategory.objects.get(id=request.POST.get('ddlsubcategory'))
            tbl_product.objects.create(product_name=request.POST.get('txtname'),
                                    product_image=request.FILES.get('fileimage'),
                                    product_details=request.POST.get('txtdescription'),
                                    product_rate=request.POST.get('txtrate'),
                                    product_type=typeid,subcat=subcateid,shop=shopid)
            return render(request,"Shop/Product.html",{'CATE':catedata,'TYPE':typedata})
        else:
            return render(request,"Shop/Product.html",{'CATE':catedata,'TYPE':typedata})
    else:
        return redirect("wguest:Userlogin")    
 

#Product details
def ProductDetail(request):
    if 'sid' in request.session:
        productdata=tbl_product.objects.all()
        return render(request,'Shop/ProductDetails.html',{'PRODUCT':productdata})
    else:
        return redirect("wguest:Userlogin")    
 
#product Delete
def del_product(request,did):
        tbl_product.objects.get(id=did).delete()
        return redirect('wshop:ProductDetail')


def Gallery(request,pid):
    if 'sid' in request.session:
        productdata=tbl_product.objects.get(id=pid)
        if request.method=='POST' and request.FILES:
            tbl_gallery.objects.create(image=request.FILES.get('fileiimage'),
                                        cation=request.POST.get('txtcaption'),product=productdata)
            return redirect('wshop:ProductDetail')
        else:
            return render(request,'Shop/Gallery.html')
    else:
        return redirect("wguest:Userlogin")    
 
#ajax subcategory


def ajax_subcategory(request):
    cate=tbl_category.objects.get(id=request.GET.get('CAT'))
    Subcate=tbl_subcategory.objects.filter(category=cate)
    return render(request,"Shop/AjaxSubcategory.html",{'SUBCATE':Subcate})


#BOOKed Products by User

def BookedProduct(request):
    if 'sid' in request.session:
        shopid=tbl_shopregistration.objects.get(id=request.session['sid'])
        bookingdata=tbl_booking.objects.filter(product__shop=shopid,booking_status=0)
        return render(request,"Shop/BookedProduct.html",{'PDATA':bookingdata})
    else:
        return redirect("wguest:Userlogin")    
 
# Accepted Order

def AcceptedOrder(request):
    if 'sid' in request.session:
        shopid=tbl_shopregistration.objects.get(id=request.session['sid'])
        bookingdata=tbl_booking.objects.filter(product__shop=shopid,booking_status=1)
        return render(request,"Shop/AcceptedOrder.html",{'PDATA':bookingdata})
    else:
        return redirect("wguest:Userlogin")    
 

def RejectedOrder(request):
    if 'sid' in request.session:
        shopid=tbl_shopregistration.objects.get(id=request.session['sid'])
        bookingdata=tbl_booking.objects.filter(product__shop=shopid,booking_status=2)
        return render(request,"Shop/RejectedOrder.html",{'PDATA':bookingdata})
    else:
        return redirect("wguest:Userlogin")    
 

#Order Accept

def OrderAccept(request,aid):
    data=tbl_booking.objects.get(id=aid)
    data.booking_status=1
    data.save()
    return redirect('wshop:BookedProduct')

#order Reject

def OrderReject(request,rid):
    data=tbl_booking.objects.get(id=rid)
    data.booking_status=2
    data.save()
    return redirect('wshop:BookedProduct')


def Complaint(request):
    if 'sid' in request.session:
        shopid=tbl_shopregistration.objects.get(id=request.session['sid'])
        complaint=tbl_complaint.objects.filter(shop=request.session['sid'])
        if request.method=='POST':
            tbl_complaint.objects.create(complaint_title=request.POST.get('complainttitle'),
                                        complaint_content=request.POST.get('complaintcontent'),
                                        shop=shopid)
            return render(request,"Shop/Complaint.html",{'DATA':complaint})
        else:
            return render(request,"Shop/Complaint.html",{'DATA':complaint})
    else:
        return redirect("wguest:Userlogin")    
 
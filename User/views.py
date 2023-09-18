from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Shop.models import *
from User.models import *


# Create your views here.

def Userhome(request):
    if 'uid' in request.session:
        data=tbl_userregister.objects.get(id=request.session['uid'])
        return render(request,"User/UserHome.html",{'Data':data})
    else:
        return redirect("wguest:Userlogin")    
   

# Myprofile

def MyProfile(request):
    if 'uid' in request.session:
        data=tbl_userregister.objects.get(id=request.session['uid'])
        return render(request,"User/Myprofile.html",{'Data':data})
    else:
        return redirect("wguest:Userlogin")    
   
#edit Profile

def Editprofile(request):
    if 'uid' in request.session:
        data=tbl_userregister.objects.get(id=request.session['uid'])
        if request.method=="POST":
            data.user_name=request.POST.get('txtname')
            data.user_contact=request.POST.get('txtcontact')
            data.user_email=request.POST.get('txtemail')
            data.user_address=request.POST.get('txtaddress')
            data.save()
            return redirect('wuser:MyProfile')
        else:
            return render(request,"User/EditProfile.html",{'Data':data})
    else:
        return redirect("wguest:Userlogin")    
   

# Change Password
def ChangePass(request):
    if 'uid' in request.session:
        data=tbl_userregister.objects.get(id=request.session['uid'])
        password=data.user_password
        if request.method=="POST":
            currentpass=request.POST.get('txtcurrentpass')
            if currentpass==password:
                newpass=request.POST.get('txtnewpass')
                confrimpass=request.POST.get('txtcomnfirmpass')
                if newpass==confrimpass:
                    data.user_password=request.POST.get('txtnewpass')
                    data.save()
                    return redirect('wu0ser:MyProfile')
            else:
                return render(request,"User/ChangePassword.html",{'msg':"Invalid Credentials!!"})
        else:
            return render(request,"User/ChangePassword.html")
    else:
        return redirect("wguest:Userlogin")    
   

#Product Details

def ProductDetail(request):
    if 'uid' in request.session:
        typedata=tbl_product_type.objects.all()
        catedata=tbl_category.objects.all()
        productdata=tbl_product.objects.all()
        return render(request,"User/Product.html",{'PRODUCT':productdata,'CATE':catedata,'TYPE':typedata})
    else:
        return redirect("wguest:Userlogin")    
   

# def ajax_subcategory(request):
#     cate=tbl_category.objects.get(id=request.GET.get('CATEGORIES'))
#     Subcate=tbl_subcategory.objects.filter(category=cate)
#     return render(request,"User/AjaxSubcategory.html",{'SUBCATE':Subcate})

def ajax_subcategory(request):
    category_ids = request.GET.get('CATEGORIES', '').split(',')
    selected_category_ids = [int(id) for id in category_ids if id.isdigit()]
    # for i in category_ids:
    #     datas=tbl_category.objects.get(id=i)
    #     result_list.append(datas.id)
    #result_list = category_ids.split(',') # Get a list of selected category IDs
    subcategories = tbl_subcategory.objects.filter(category__in=selected_category_ids)
    return render(request, "User/AjaxSubcategory.html", {'SUBCATE': subcategories})



def Ajax_Product(request):
    if request.GET.get("tid")!="":
        typeid=tbl_product_type.objects.get(id=request.GET.get('tid'))
        productdata=tbl_product.objects.filter(product_type=typeid)
        return render(request,"User/AjaxProduct.html",{'PRODUCT':productdata})
    # elif request.GET.get("cid")!="":
    #     catid=tbl_category.objects.get(id=request.GET.get('cid'))
    #     productdata=tbl_product.objects.filter(subcat__category=catid)
    #     return render(request,"User/AjaxProduct.html",{'PRODUCT':productdata})



def ProductGallery(request,pid):
    if 'uid' in request.session:
        productdata=tbl_product.objects.get(id=pid)
        gallerydata=tbl_gallery.objects.filter(product=pid)
        return render(request,'User/Gallery.html',{'DATA':productdata,'GALLERY':gallerydata})
    else:
        return redirect("wguest:Userlogin")    
          

#Product Booking

def Productbooking(request,pid):
    if 'uid' in request.session:
        userid=tbl_userregister.objects.get(id=request.session['uid'])
        productid=tbl_product.objects.get(id=pid)
        productdata=tbl_product.objects.get(id=pid)
        if request.method=='POST':
            tbl_booking.objects.create(booking_quantity=request.POST.get('quantity'),
                                total_amount=request.POST.get('txtamount'),
                                user=userid,product=productid)
            return render(request,'User/Booking.html',{'PDATA':productdata})
        else:
            return render(request,'User/Booking.html',{'PDATA':productdata})
    else:
        return redirect("wguest:Userlogin")    
           


#booked product

def Bookedproduct(request):
    if 'uid' in request.session:
        userid=tbl_userregister.objects.get(id=request.session['uid'])
        productdata=tbl_booking.objects.filter(user=userid)
        return render(request,'User/BookedProduct.html',{'PDATA':productdata})
    else:
        return redirect("wguest:Userlogin")    
   
def Complaint(request):
    if 'uid' in request.session:
        userid=tbl_userregister.objects.get(id=request.session['uid'])
        complaint=tbl_complaint.objects.filter(user=request.session['uid'])
        if request.method=='POST':   
            tbl_complaint.objects.create(complaint_title=request.POST.get('complainttitle'),
                                        complaint_content=request.POST.get('complaintcontent'),user=userid)
            return render(request,"User/Complaint.html",{'DATA':complaint})
        else:
            return render(request,"User/Complaint.html",{'DATA':complaint})
    else:
        return redirect("wguest:Userlogin")    
           
def Feedback(request):
    if 'uid' in request.session:
        userid=tbl_userregister.objects.get(id=request.session['uid'])
        if request.method=='POST':
            tbl_feedback.objects.create(feedback=request.POST.get('feedback'),user=userid) 
            return render(request,"User/Feedback.html")
        else:
            return render(request,"User/Feedback.html")
    else:
        return redirect("wguest:Userlogin")    
   
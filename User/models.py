from django.db import models
from Guest.models import *
from Shop.models import *

# Create your models here.

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now=True)
    booking_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_userregister,on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    booking_quantity=models.IntegerField(null=False)
    total_amount=models.IntegerField(null=False)

class tbl_complaint(models.Model):
    complaint_date=models.DateField(auto_now=True)
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=100)
    complaint_reply=models.CharField(max_length=100,default="No Reply yet")
    user=models.ForeignKey(tbl_userregister,on_delete=models.CASCADE,null=True)
    shop=models.ForeignKey(tbl_shopregistration,on_delete=models.CASCADE,null=True)
    complaint_status=models.IntegerField(default=0,null=True)

class tbl_feedback(models.Model):
    feedback_date=models.DateField(auto_now=True)
    feedback=models.CharField(max_length=100)
    user=models.ForeignKey(tbl_userregister,on_delete=models.CASCADE,null=True)
    shop=models.ForeignKey(tbl_shopregistration,on_delete=models.CASCADE,null=True)
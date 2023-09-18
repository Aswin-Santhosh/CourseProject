from django.db import models
from Admin.models import *
# Create your models here.

class tbl_userregister(models.Model):
    user_name=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.EmailField(unique=True)
    user_address=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='userdocs/',null=True)
    user_password=models.CharField(max_length=50,unique=True)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True)


class tbl_shopregistration(models.Model):
    shop_name=models.CharField(max_length=50)
    owner_name=models.CharField(max_length=50)
    shop_contact=models.CharField(max_length=50)
    shop_email=models.EmailField(unique=True)
    shop_address=models.CharField(max_length=100)
    shop_logo=models.FileField(upload_to='shopdocs/',null=True)
    shop_proof=models.FileField(upload_to='shopproof/',null=True)
    shop_since=models.CharField(max_length=50)
    shop_password=models.CharField(max_length=50,unique=True)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True)
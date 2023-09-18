from django.db import models

# Create your models here.


class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)



class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
    
class tbl_product_type(models.Model):
    product_type=models.CharField(max_length=50)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE,null=True)

class tbl_adminregister(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.EmailField(unique=True)
    admin_password=models.CharField(max_length=50,unique=True)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    place_pin=models.CharField(max_length=10)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE,null=True)
    
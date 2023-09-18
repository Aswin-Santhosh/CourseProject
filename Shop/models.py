from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class tbl_product(models.Model):
    product_name=models.CharField(max_length=50)
    product_image=models.FileField(upload_to="ProductDocs/")
    product_details=models.CharField(max_length=150)
    product_rate=models.CharField(max_length=50)
    # product_type=models.CharField(max_length=10,null=True)
    product_type=models.ForeignKey(tbl_product_type,on_delete=models.CASCADE,null=True)
    subcat=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE,null=True)
    shop=models.ForeignKey(tbl_shopregistration,on_delete=models.CASCADE,null=True)


class tbl_gallery(models.Model):
    image=models.FileField(upload_to="ProductDocs/ProductGallery/")
    cation=models.FileField(max_length=100)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE,null=True)
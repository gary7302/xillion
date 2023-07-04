
from django.db import models
from django.contrib.auth.models import User
import os
import datetime

# Create your models here.
def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('uploads/',filename)


class Product(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=10000)
    price=models.FloatField()
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100,null=False)
    lname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    mobilenumber=models.IntegerField(max_length=100,null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=100, null=False)
    state= models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.IntegerField(null=False)
    cancer=models.FileField(null=False)
    proof=models.FileField(null=False)
    letter=models.FileField(null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=250,null=True)
    orderstatus=(
        ('pending','pending'),('Out For Delivery','Out For Delivery'),('completed','completed')
    )
    status=models.CharField(max_length=150,choices=orderstatus,default='pending')
    message=models.TextField(null=True)
    tracking_no=models.CharField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)

class Orderitems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id,self.order.tracking_no)

class Profil(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobilenumber = models.IntegerField(null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.IntegerField(null=False)
    cancer=models.FileField(null=False)
    proof=models.FileField(null=False)
    letter=models.TextField(max_length=1000, null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="comments")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_chinese(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('chinese_uploads/',filename)

class ChineseProduct(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_chinese,null=True,blank=True)
    description=models.TextField(max_length=10000)
    price=models.FloatField()
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class ChineseComment(models.Model):
    product=models.ForeignKey(ChineseProduct,on_delete=models.CASCADE,related_name="chinesecomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_chinese,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

class ChineseCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(ChineseProduct,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
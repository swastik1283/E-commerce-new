from django.db import models

from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.contrib.auth.models import User

choice_field = (
    ('sr','shirt'),
    ('pn','pant'),
    ('ct','coat'),
    ('lw','lower'),
    ('ts','tshirt'),
    ('kt','kurta'),
    ('hs','hosiery'),
)

choice_state = (
    ("Andhra Pradesh","Andhra Pradesh"),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Chandigarh','Chandigarh'),
    ('Delhi','Delhi'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
)

class Products(models.Model):
    prod_title = models.CharField(max_length=50)
    prod_price = models.FloatField()
    prod_discount = models.FloatField()
    prod_disc = HTMLField()
    prod_color = models.CharField(max_length=50)
    prod_size = models.CharField(max_length=50)
    prod_cata = models.CharField(choices = choice_field,max_length=2)
    prod_img = models.FileField( upload_to="Products", max_length=500,null=True,default = None)
    prod_slug = AutoSlugField(populate_from = "prod_title" , unique = True , null =True , default = None)

    def __str__(self):
        return self.prod_title

    def disp(self):
        disp = int((self.prod_discount / self.prod_price ) * 100)
        return disp
    
    def pricc(self):
        pricc = int((self.prod_price - self.prod_discount ) )
        return pricc
    
class customerdetail(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    mobile = models.IntegerField(default =0)
    pincode = models.IntegerField()
    state = models.CharField(choices = choice_state,max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    Product1 = models.ForeignKey(Products,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        total_cost =  self.quantity * self.product1.pricc
        return total_cost
# Create your models here.

status_choice = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancelled','Cancelled'),
    ('Pending','Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length = 100 , blank =True , null = True)
    razorpay_payment_status = models.CharField(max_length = 100 , blank =True , null = True)
    razorpay_payment_id = models.CharField(max_length = 100 , blank =True , null = True)
    paid = models.BooleanField(default = False)

class Orderplaced(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    customer = models.ForeignKey(customerdetail,on_delete = models.CASCADE)
    product = models.ForeignKey(Products,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    order_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50 ,choices = status_choice, default = "pending")
    payment  = models.ForeignKey(Payment,on_delete = models.CASCADE , default = "")
    @property
    def total_cost(self):
        total_cost =  self.quantity * self.product1.pricc
        return total_cost
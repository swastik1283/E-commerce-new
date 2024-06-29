from django.contrib import admin
from product.models import Products,customerdetail,Cart,Payment,Orderplaced

class prod_admin(admin.ModelAdmin):
    list_display = ('prod_title','prod_price','pricc','prod_discount','prod_disc', 'prod_color','prod_size','disp','prod_cata', 'prod_img','prod_slug')
admin.site.register(Products,prod_admin)

class customer_admin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','mobile','pincode','state']
admin.site.register(customerdetail,customer_admin)

class Cart_admin(admin.ModelAdmin):
    list_display = ['id','user','Product1','quantity']
admin.site.register(Cart,Cart_admin)

class payment_admin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']
admin.site.register(Payment,payment_admin)

class order_admin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','order_date','status','payment']
admin.site.register(Orderplaced,order_admin)

# Register your models here.

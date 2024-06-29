from django.shortcuts import render ,HttpResponseRedirect,redirect
from django.http import HttpResponse, JsonResponse
from product.models import Products,customerdetail,Cart,Payment,Orderplaced
from contact_us.models import Contact
from .form import registrationform,loginform,customerprofile,password_change_1
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.views import View
from django.db.models import Q
from django.conf import settings
import razorpay

def home(request):

    return render(request,"index.html")

def catagory(request,val):
    productt = Products.objects.filter(prod_cata = val)
    data = {
        "products":productt,
    }
    return render(request,"catagory.html",data)

def product_detail(request,slug1):
    p_data = Products.objects.get(prod_slug= slug1)
    data = {
        'p_data':p_data,
    }
    return render(request,"product_detail.html",data)

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method =="POST":
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        topic = request.POST.get("topic")
        order = request.POST.get("order")
        comment = request.POST.get("comment")
        if email=="" or telephone=="" or topic=="" or order=="" or comment=="":
            return render(request,"contact.html",{"error":True})
        st = Contact(email =email, phone =telephone ,issue = topic,order_no = order , message = comment) 
        st.save()
        return render(request,"contact.html",{"success1":True})
    return render(request,"contact.html")

def registration(request):
    fm = registrationform()
    if request.method =="POST":
        fm = registrationform(request.POST)
        if fm.is_valid():
            messages.success(request,"Successfully Registered")
            fm.save()
    else:
        fm = registrationform()
        messages.error(request,"Invalid Input Data")
        return render(request,"registration.html",{'form1':fm})
    return render(request,"registration.html",{'form1':fm})

def loginf(request):    
    if request.method =="POST":
        fm = loginform(request=request,data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username = uname,password = upass)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully Login")
                return HttpResponseRedirect('/profile/')
            
    else:
        fm = loginform()
        messages.error(request,"Invalid Input Data")
    return render(request,"login.html",{'form1':fm})

def password_reset_1(request):
    if request.method =="POST":
        fm = password_change_1(user=request.user,data = request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Successfully Password Changed")
            return render(request,"password_change.html",{'form':fm})
    else:
        fm = password_change_1(user=request.user)
    return render(request,"password_change.html",{'form':fm})

def profile(request):
    fm = customerprofile()
    if request.method =="POST":
        fm = customerprofile(request.POST)
        if fm.is_valid():
            user = request.user
            name = fm.cleaned_data["name"]
            locality = fm.cleaned_data["locality"]
            city = fm.cleaned_data["city"]
            mobile = fm.cleaned_data["mobile"]
            pincode = fm.cleaned_data["pincode"]
            state = fm.cleaned_data["state"]
            dataa = customerdetail(user=user,name=name,locality=locality,city=city,mobile=mobile,pincode=pincode,state=state)
            dataa.save()
            messages.success(request,"Successfully Profile Saved")
        else:
            messages.warning(request,"Invalid Input Data")
    return render(request,"profile.html",{'form1':fm})

def address(request):
    add = customerdetail.objects.filter(user = request.user)
    if add is not None:
        return render(request,"address.html",{'add':add })
    else:
        return render(request,"address.html",{'error1':True })
    # return render(request,"address.html",{'add':add })

class updateaddress(View):
    def get(self,request,pk):
        add = customerdetail.objects.get(pk=pk)
        fm = customerprofile(instance=add)
        return render(request,"updateaddress.html",{'form1':fm})
    def post(self,request,pk):
        fm = customerprofile(request.POST)
        if fm.is_valid():
            user = request.user
            name = fm.cleaned_data["name"]
            locality = fm.cleaned_data["locality"]
            city = fm.cleaned_data["city"]
            mobile = fm.cleaned_data["mobile"]
            pincode = fm.cleaned_data["pincode"]
            state = fm.cleaned_data["state"]
            dataa = customerdetail(id = pk ,user=user,name=name,locality=locality,city=city,mobile=mobile,pincode=pincode,state=state)
            dataa.save()
            messages.success(request,"Successfully Profile Updated")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('address')
    
def add_to_cart(request):
    user = request.user
    prod_id = request.GET.get('prod_id')
    product = Products.objects.get(id = prod_id)
    data = Cart(user = user , Product1 = product)
    data.save()
    return redirect('/cart')

def showcart(request):
    user = request.user
    cart  = Cart.objects.filter(user = user)
    amount = 0
    for itemss in cart:
        value = itemss.quantity * itemss.Product1.pricc()
        amount= amount + value
    totalamount = amount + 40 
    
    return render(request,"addtocart.html",locals())

def plus_cart(request):
    if request.method=="GET":
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(Product1 = prod_id) & Q(user = request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        for itemss in cart:
            value = itemss.quantity * itemss.Product1.pricc()
            amount= amount + value
        totalamount = amount + 40 
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method=="GET":
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(Product1 = prod_id) & Q(user = request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        for itemss in cart:
            value = itemss.quantity * itemss.Product1.pricc()
            amount= amount + value
        totalamount = amount + 40 
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method=="GET":
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(Product1 = prod_id) & Q(user = request.user))
        c.quantity=0
        c.delete
        c.save()
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        for itemss in cart:
            value = itemss.quantity * itemss.Product1.pricc()
            amount= amount + value
        totalamount = amount + 40 
        data = {
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def checkout(request):
    user = request.user
    add = customerdetail.objects.filter(user = user)
    cartitem = Cart.objects.filter(user = user)
    amount = 0
    for itemss in cartitem:
        value = itemss.quantity * itemss.Product1.pricc()
        amount= amount + value
    totalamount = amount + 40 
    # razoramount = int(totalamount*100)
    # client = razorpay.Client
    # # data = {
    # #         'amount':amount,
    # #         'totalamount':totalamount
    # #     }
    # data = {"amount":razoramount,"currency":"INR","receipt":"order_reptid_12"}
    # payment_response = client.order.create(data = data)
    # print(payment_response)
    # order_id = payment_response['id']
    # order_status = payment_response['status']
    # if order_status == "created":
    #     payment = Payment(
    #         user = user,
    #         amount = totalamount,
    #         razorpay_payment_status = order_status,
    #         razorpay_order_id = order_id
    #     )
    #     payment.save()
    return render(request,"checkout.html",locals())
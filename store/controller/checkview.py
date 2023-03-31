from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User

@login_required(login_url='loginpage')
def checkout(request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.quantity > item.product.quantity:
            Cart.objects.delete(id=item.id)

    cartitems=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price=total_price+item.product.price*item.quantity

    userprofile=Profile.objects.filter(user=request.user).first()

    context={'cartitems':cartitems,'total_price':total_price,'userprofile':userprofile}
    return render(request,'store/checkout.html',context)

@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == "POST":
        currentuser=User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name=request.POST.get('fname')
            currentuser.last_name=request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile=Profile()
            userprofile.user=request.user
            userprofile.mobilenumber = request.POST.get('mobilenumber')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()


        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.mobilenumber = request.POST.get('mobilenumber')
        neworder.address = request.POST.get('address')
        neworder.city= request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')
        neworder.payment_mode=request.POST.get('payment_mode')

        cart=Cart.objects.filter(user=request.user)
        cart_total_price=0
        for item in cart:
            cart_total_price=cart_total_price+item.product.price * item.quantity

        neworder.total_price=cart_total_price
        trackno='gary'+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno='gary'+str(random.randint(1111111,9999999))

        neworder.tracking_no=trackno
        neworder.save()

        neworderitems=Cart.objects.filter(user=request.user)
        for item in neworderitems:
            Orderitems.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )

            # to decrese quantity from available stock
            orderproduct=Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity= orderproduct.quantity-item.quantity
            orderproduct.save()

        # to clear cart for user
        Cart.objects.filter(user=request.user).delete()

        messages.success(request,"Order Placed Successfully")


    return redirect("/")
from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:

            product_id_str=request.POST.get('product_id')
            if product_id_str is not None:
                prod_id = int(product_id_str)
            else:
                return JsonResponse({'status': 'Product already in Cart'+str(product_id_str)})

            product_check=Product.objects.get(id=prod_id)
            if product_check:
                if(Cart.objects.filter(user_id=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':'Product already in Cart'})
                else:
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,quantity=prod_qty)
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':'Only '+str(product_check.quantity)+' quantity available'})
            else:
                return JsonResponse({'status':'No such product found'})
        else:
            return JsonResponse({'status':'Login to Continue'})
    else:
        return redirect('/')
@login_required(login_url='loginpage')
def showCart(request):
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,'store/cart.html',context)
@csrf_exempt
def updatecart(request):
    if request.method == "POST":
        product_id_str = request.POST.get('product_id')
        if product_id_str is not None:
            prod_id = int(product_id_str)
        else:
            return JsonResponse({'status': 'Product already in Cart' + str(product_id_str)})

        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty=request.POST.get('product_qty')
            cart=Cart.objects.get(user=request.user,product_id=prod_id)
            cart.quantity=prod_qty
            cart.save()
            return JsonResponse({'status':'Updated Successfully'})
    return redirect('/')

def deletecartitem(request):
    if request.method == "POST":
        prod_id=int(request.POST.get('product_id'))
        cartitem=Cart.objects.get(user=request.user,product_id=prod_id)
        cartitem.delete()
        return JsonResponse({'status':'Deleted Successfully'})
    return redirect('/')

def chineseaddtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:

            product_id_str=request.POST.get('product_id')
            if product_id_str is not None:
                prod_id = int(product_id_str)
            else:
                return JsonResponse({'status': 'Product already in Cart'+str(product_id_str)})

            product_check=ChineseProduct.objects.get(id=prod_id)
            if product_check:
                if(ChineseCart.objects.filter(user_id=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':'Product already in Cart'})
                else:
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        ChineseCart.objects.create(user=request.user,product_id=prod_id,quantity=prod_qty)
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':'Only '+str(product_check.quantity)+' quantity available'})
            else:
                return JsonResponse({'status':'No such product found'})
        else:
            return JsonResponse({'status':'Login to Continue'})
    else:
        return redirect('/')

@login_required(login_url='chineselogin')
def chineseshowCart(request):
    cart=ChineseCart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,'chinese-store/cart.html',context)

@csrf_exempt
def chineseupdatecart(request):
    if request.method == "POST":
        product_id_str = request.POST.get('product_id')
        if product_id_str is not None:
            prod_id = int(product_id_str)
        else:
            return JsonResponse({'status': 'Product already in Cart' + str(product_id_str)})

        if(ChineseCart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty=request.POST.get('product_qty')
            cart=ChineseCart.objects.get(user=request.user,product_id=prod_id)
            cart.quantity=prod_qty
            cart.save()
            return JsonResponse({'status':'Updated Successfully'})
    return redirect('/chinese')

def chinesedeletecartitem(request):
    if request.method == "POST":
        prod_id=int(request.POST.get('product_id'))
        cartitem=ChineseCart.objects.get(user=request.user,product_id=prod_id)
        cartitem.delete()
        return JsonResponse({'status':'Deleted Successfully'})
    return redirect('/chinese')
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    category=Category.objects.all()
    return render(request,'store/index.html',{'category':category})

def type(request,slug):
    if(Category.objects.filter(slug=slug)):
        product=Product.objects.filter(category__slug=slug)
        category_name=Category.objects.filter(slug=slug)
        context={'product':product,'category':category_name}
        return render(request,'store/products/index.html',context)
    else:
        messages.warning(request,'No such category found')
        return redirect('home')

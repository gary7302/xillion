from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from datetime import datetime
from .forms import *
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    product=Product.objects.all()
    return render(request,'store/products/index.html',{'product':product})

# def type(request,slug):
#     if(Category.objects.filter(slug=slug)):
#         product=Product.objects.filter(category__slug=slug)
#         category_name=Category.objects.filter(slug=slug)
#         context={'product':product,'category':category_name}
#         return render(request,'store/products/index.html',context)
#     else:
#         messages.warning(request,'No such category found')
#         return redirect('home')

def comment(request,id):
    eachProduct = Product.objects.get(id=id)


    form = CommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'store/coment.html',context)

def addComment(request,id):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = Product.objects.get(id=id)
            c = Comment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                        comment_image=comment_image, created_at=datetime.now())
            c.save()
            return redirect('/')
    return HttpResponse('<h1>We are unable to add your comment</h1>')

def getpatch(request):
    return render(request,'store/getpatch.html')

def usepatch(request):
    return render(request,'store/usepatch.html')

def details(request):
    return render(request,'store/details.html')
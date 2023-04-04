from django.urls import path
from .views import *
from store.controller import authview,cartview,checkview,paymentview

urlpatterns = [
    path('',home,name='home'),
    path('type/<str:slug>',type,name='type'),
    path('register',authview.register,name='register'),
    path('login',authview.loginpage,name='loginpage'),
    path('logout',authview.logoutpage,name='logoutpage'),
    path('add-to-cart',cartview.addtocart,name='addtocart'),
    path('cart',cartview.showCart,name='cart'),
    path('update-cart',cartview.updatecart,name="updatecart"),
    path('delete-cart-item',cartview.deletecartitem,name="deletecartitem"),
    path('checkout',checkview.checkout,name='checkout'),
    path('place-order',checkview.placeorder,name="placeorder"),
    path('charge', paymentview.charge, name='charge'),
    path('success/', paymentview.success, name='success'),
    path('type/comment/<int:id>/', comment, name='comment'),
    path('addComment/<int:id>', addComment, name='addComment'),
]
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Orderitems)
admin.site.register(Profil)
admin.site.register(ChineseProduct)
admin.site.register(Comment)
admin.site.register(ChineseComment)
admin.site.register(ChineseCart)
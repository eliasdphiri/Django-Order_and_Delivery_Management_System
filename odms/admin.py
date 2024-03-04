from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Salesrep,Stkitem, Tills, Whsemst, Whsestk, Etblwhsetransferbatchlines, Etblwhsetransferbatches

admin.site.site_header = 'Yalelo ODMS Admin Panel'

# class ProductAdmin(admin.ModelAdmin):
  #  list_display = ('name', 'category','weight')
   # list_filter = ['category']

# Register your models here.

# admin.site.register(Product,ProductAdmin)
# admin.site.register(Order)

# admin.site.unregister(Group)

from django.db import models
from django.contrib import admin
class customer_db(models.Model):
    Vehicle_no=models.CharField(max_length=10,primary_key=True)
    Owner_name=models.CharField(max_length=40)
    Insurance_no=models.IntegerField()
    Address=models.TextField()
    Mobile=models.IntegerField()
    Service_no=models.IntegerField()
class customer_dbAdmin(admin.ModelAdmin):
    list_display=["Vehicle_no","Owner_name","Insurance_no","Address","Mobile","Service_no"]
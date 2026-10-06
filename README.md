# Ex02 Django ORM Web Application
## Date: 06.10.2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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


admin.py
from django.contrib import admin
from .models import customer_db,customer_dbAdmin
admin.site.register(customer_db,customer_dbAdmin)


```


## OUTPUT
![alt text](image.png)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully

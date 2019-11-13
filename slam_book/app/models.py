from django.db import models
from datetime import date

class Admin_Login1(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=30)


class User_Login1(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=30)
    phone_number = models.IntegerField()

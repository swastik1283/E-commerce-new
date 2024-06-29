from django.db import models
from tinymce.models import HTMLField

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length = 50)
    issue = models.CharField(max_length = 50)
    order_no = models.CharField(max_length = 50)
    message = models.CharField(max_length = 250)

class registration(models.Model):
    name1= models.CharField(max_length = 50)
    contact = models.CharField(max_length = 50)
    email = models.EmailField()
    pin = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    add1 = HTMLField()
# Create your models here.

from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)
    def __str__(self):
        return self.name
    
class Stock(models.Model):
    name=models.CharField(max_length=30)
    symbol=models.CharField(max_length=30)
    desc=models.CharField(max_length=10000)
    slug=AutoSlugField(populate_from="id",unique=True,null=True,default=None)
    def __str__(self):
        return self.name
    
class Query(models.Model):
    name=models.ForeignKey(Users,on_delete=models.CASCADE)
    user=models.CharField(max_length=20,default="default")
    query=models.CharField(max_length=400)
    stock_regarding=models.CharField(max_length=400,default="default")
    
     
    def __str__(self):
        return (self.user)
    
    

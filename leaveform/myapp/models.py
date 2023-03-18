from django.db import models
from datetime import datetime

# Create your models here.
class Details(models.Model):
    username =  models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    rno =  models.CharField(max_length=100, blank=True)
    ug=  models.CharField(max_length=100, blank=True)
    year=  models.CharField(max_length=100, blank=True)
    section=  models.CharField(max_length=100, blank=True)
    course =  models.CharField(max_length=100, blank=True)
    tot= models.IntegerField(blank=True, null=True)
    leaveletter= models.IntegerField(blank=True, null=True)
    medical = models.IntegerField(blank=True, null=True)
    absent= models.IntegerField(blank=True, null=True)
    previlege= models.IntegerField(blank=True, null=True)
    relation= models.CharField(max_length=100, blank=True)
    totdays= models.IntegerField(blank=True, null=True)
    reason =  models.IntegerField(max_length=100, blank=True)
    date= models.IntegerField(blank=True, null=True)
    froms=  models.IntegerField(blank=True, null=True)
    tos=models.IntegerField(blank=True, null=True)
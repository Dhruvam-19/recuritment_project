from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    company_name = models.CharField(max_length=100,blank=True,null=True)
    gst_number = models.CharField(max_length=100,blank=True,null=True)
    ho_address = models.TextField(blank=True,null=True)
    plant_address = models.TextField(blank=True,null=True)
    state = models.CharField(max_length=30,blank=True,null=True)
    country = models.CharField(max_length=25,blank=True,null=True)
    phone_number = models.CharField(max_length=12,blank=True,null=True)
    contact_person1_name = models.CharField(max_length=40,blank=True,null=True)
    contact_person2_name = models.CharField(max_length=40, blank=True, null=True)
    contact_person1_number = models.CharField(max_length=12, blank=True, null=True)
    contact_person2_number = models.CharField(max_length=12,blank=True, null=True)
    date_of_signing = models.DateField(blank=True, null=True)
    fees = models.IntegerField(blank=True, null=True)
    replacement_period = models.CharField(max_length=20,blank=True, null=True)
    payment_term = models.CharField(max_length=30,blank=True, null=True)
    validity_of_resume = models.CharField(max_length=30,blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=40,blank=True, null=True)
    current_status = models.CharField(max_length=20,blank=True, null=True)
    agreement1 = models.FileField(upload_to='company_agreement', null=True, blank=True)
    agreement2 = models.FileField(upload_to='other_agreement',blank=True, null=True)

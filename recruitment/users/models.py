from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pic')
    first_name = models.CharField(max_length=30,blank=True,null=True)
    middle_name = models.CharField(max_length=30,blank=True,null=True)
    last_name = models.CharField(max_length=30,blank=True,null=True)
    father_first_name = models.CharField(max_length=100,blank=True,null=True)
    father_middle_name = models.CharField(max_length=100,blank=True,null=True)
    father_last_name = models.CharField(max_length=100,blank=True,null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    resignation_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True,null=True)
    phone_number1 = models.CharField(max_length=11,blank=True,null=True)
    phone_number2 = models.CharField(max_length=11, blank=True,null=True)
    address_lane1 = models.CharField(max_length=100,blank=True,null=True)
    address_lane2 = models.CharField(max_length=100,blank=True,null=True)
    address_lane3 = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    bank_name = models.CharField(max_length=100,blank=True,null=True)
    bank_branch = models.CharField(max_length=100,blank=True,null=True)
    pan_number = models.CharField(max_length=50,blank=True,null=True)
    account_number = models.CharField(max_length=50,blank=True,null=True)
    ifsc_code = models.CharField(max_length=50,blank=True,null=True)
    micr_code = models.CharField(max_length=50,blank=True,null=True)
    adharcard_number = models.CharField(max_length=50,blank=True,null=True)
    document1 = models.ImageField(default='default.jpg',upload_to='documents', null=True, blank=True)
    document2 = models.ImageField(default='default.jpg',upload_to='documents', null=True, blank=True)
    document3 = models.ImageField(default='default.jpg',upload_to='documents', null=True, blank=True)
    execution = models.IntegerField(blank=True,null=True)
    bd = models.IntegerField(blank=True,null=True)
    agreement_document = models.ImageField(default='default.jpg',upload_to='agreement', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} profile"

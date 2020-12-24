from django.db import models
from django.contrib.auth.models import User
from company.models import Company
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Candidate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    industry = models.CharField(max_length=100,blank=True,null=True)
    profile_name = models.CharField(max_length=100, blank=True, null=True)
    candidate_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    current_designation = models.CharField(max_length=100, blank=True, null=True)
    current_organisation = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    current_ctc = models.CharField(max_length=100, blank=True, null=True)
    expected_ctc = models.CharField(max_length=100, blank=True, null=True)
    notice_period = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    email_id = models.EmailField(blank=True,null=True, unique=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True, unique=True)
    cv = models.FileField(upload_to='cv',blank=True, null=True)
    date =models.DateTimeField(default=timezone.now,verbose_name="Date")

    def get_absolute_url(self):
        return reverse('company-home')

    def __str__(self):
        return f"{self.candidate_name}"
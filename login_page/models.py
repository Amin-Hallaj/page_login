from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import  User , Permission


class MemberRegistration(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="member_registration")
    national_code=models.CharField(max_length=10)
    first_name_last_name=models.CharField(max_length=200)
    gmail=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=13)

    def __str__(self):
        return self.fullname

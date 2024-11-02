from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = PhoneField(blank=False, help_text='Contact Phone Number')
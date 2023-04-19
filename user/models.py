from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime


class CustomUser(AbstractUser):

    name = models.CharField(max_length=30, null=True, blank=True)
    mobile = models.CharField(
        ('Mobile Number'), max_length=14, null=True, blank=True)
    registered = models.BooleanField(default=False)
    email = models.EmailField(
        _("Email address"), null=True, blank=True, unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('D', 'Not Given'),
    )
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=True, blank=True, default='D')
    birthdate = models.DateField(blank=True, null=True)

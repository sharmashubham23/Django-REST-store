from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from user.models import *


class Products(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(default=datetime.datetime.today)


class Orders(models.Model):
    cu = models.ForeignKey(
        CustomUser, default=None, on_delete=models.CASCADE)
    pro = models.ForeignKey(
        Products, default=None, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today)


class Cart(models.Model):
    cu = models.ForeignKey(
        CustomUser, default=None, on_delete=models.CASCADE)
    pro = models.ForeignKey(
        Products, default=None, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today)

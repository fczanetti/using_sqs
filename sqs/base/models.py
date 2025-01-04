from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

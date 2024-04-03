from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    address = models.CharField(max_length=500)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    apartment = models.IntegerField(null=True, blank=True)
    entrance = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)

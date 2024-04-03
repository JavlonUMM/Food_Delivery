from django.db import models


class Branch(models.Model):
    address = models.TextField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

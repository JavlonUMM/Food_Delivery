from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, related_name='customer_profile')
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.full_name
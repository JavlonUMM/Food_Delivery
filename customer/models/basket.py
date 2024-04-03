from django.db.models import (Model, ForeignKey, CASCADE, IntegerField, BooleanField)
from django.core.validators import MaxLengthValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Basket(Model):
    customer = ForeignKey(User, CASCADE)
    product = ForeignKey('product.models.Product', CASCADE)
    quantity = IntegerField(validators=[MinValueValidator(1)])
    is_ordered = BooleanField(default=True)

    def __str__(self):
        return self.customer

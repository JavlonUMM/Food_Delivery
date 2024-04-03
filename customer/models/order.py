from django.contrib.auth import get_user_model
from django.db.models import (Model, BooleanField, ForeignKey, CASCADE, DateTimeField)
from django.utils import timezone

User = get_user_model()


class Order(Model):
    customer = ForeignKey(User, CASCADE, related_name='customer_order')
    basket = ForeignKey('customer.basket.Basket', CASCADE)
    is_ordered = BooleanField(default=True)
    create_at = DateTimeField(auto_now_add=timezone.now)
    is_deliver = BooleanField()
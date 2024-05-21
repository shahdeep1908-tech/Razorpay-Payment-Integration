from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField


class Payment(models.Model):
    event = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    phone_number = PhoneField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.order_id

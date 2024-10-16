from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from base.models.helpers.date_time_model import DateTimeModel

class CustomerModel(AbstractUser, DateTimeModel):
    number = models.CharField(max_length=15, unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customer_users',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_permissions',  
        blank=True
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.username

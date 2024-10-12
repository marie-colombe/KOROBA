from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class CartModel(DateTimeModel):
    STATUS_CHOICES = [
        ('open', 'En cours'),
        ('checked_out', 'Validé'),
        ('abandoned', 'Abandoné'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"Cart {self.id} - Status: {self.status}"

    @property
    def total_price(self):
        items = self.cartsitemmodel_set.all()
        return sum(item.total_price for item in items)


      







    
    



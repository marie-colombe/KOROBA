from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from customer.models.customer_model import CustomerModel


class CartModel(DateTimeModel):
    customer = models.OneToOneField(CustomerModel, on_delete=models.CASCADE, related_name='cart')

    class Meta:
        verbose_name = "cart"
        verbose_name_plural = "carts"


      







    
    



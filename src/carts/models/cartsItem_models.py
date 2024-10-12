from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from product.models.product_model import ProductModel
from carts.models.cart_model import CartModel



class CartsItemModel(DateTimeModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, null=True, blank=True, related_name='items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Item {self.product.name_product} - Quantity: {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity



      

from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from artisan.models.artisan_model import ArtisanModel
from django.contrib.auth.models import Group, Permission

class ProductModel(DateTimeModel):
    artisan = models.ForeignKey(ArtisanModel, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=50)
    description_product = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product/images')

    groups = models.ManyToManyField(
        Group,
        related_name='product_users',  # Nom unique pour éviter les conflits
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='product_permissions',  # Nom unique pour éviter les conflits
        blank=True
    )

    def __str__(self):
        return self.name_product

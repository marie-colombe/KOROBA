from django.db import models

from base.models.helpers.date_time_model import DateTimeModel

class PersonModel(DateTimeModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    #gender = models.CharField(max_length=10, choices=gender_model.Gender.choices)
    

    
    class Meta:
        abstract = True
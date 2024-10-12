from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from django.contrib.auth.models import AbstractUser

from management import settings

SEX = [
    ('M', 'Male'),
    ('F', 'Female'),
    
]

WORK =[

    ('Coiffure', 'Coiffure'),
    ('Couture', 'Couture'),
    ('Mecanique', 'Mecanique'),
    ('Bijouterie', 'Bijouterie'),
    ('Maconnerie', 'Maconnerie'),
    ('Transport', 'Transport'),
    ('Electronique', 'Electronique'),
    ('Boucherie', 'Boucherie'),

]

class ArtisanModel(AbstractUser,DateTimeModel):
    work = models.CharField(max_length=255, choices=WORK)
    sex = models.CharField(max_length=1, choices=SEX)
    number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    identity_document = models.ImageField(upload_to='artisan/identity_docs', blank=True, null=True)
    confidenciality = models.BooleanField(default=False)
    pseudo = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='artisan/pictures/', blank=True, null=True)

    @property
    def picture_url(self):
        if self.picture:
            return f"{settings.MEDIA_URL}{self.picture}"
        return None

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='artisan_groups',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='artisan_permissions',
        blank=True
    )
    
    def __str__(self):
        return self.username



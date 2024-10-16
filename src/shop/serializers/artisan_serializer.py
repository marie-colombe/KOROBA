from rest_framework import serializers
from shop.models.artisan_model import ArtisanModel

class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtisanModel
        fields = ['id', 'username', 'work', 'sex', 'number', 'whatsapp_number', 'pseudo', 'picture', 'password']
        extra_kwargs = {'password': {'write_only': True}}



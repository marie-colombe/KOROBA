from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from shop.models.artisan_model import ArtisanModel
from shop.serializers.artisan_serializer import ArtisanSerializer

class ArtisanViewSet(viewsets.ModelViewSet):
    queryset = ArtisanModel.objects.all()
    serializer_class = ArtisanSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password', None) 
        artisan = serializer.save() 
        if password:
            artisan.set_password(password)  
            artisan.save()

    def perform_update(self, serializer):
        """Surcharge de la méthode update pour gérer la mise à jour du mot de passe"""
        password = serializer.validated_data.pop('password', None)
        artisan = serializer.save() 
        if password:
            artisan.set_password(password) 
            artisan.save()
    
    @action(detail=False, methods=['get'], url_path='by-work/(?P<work>[^/.]+)')
    def filter_by_work(self, request, work=None):
        artisans = ArtisanModel.objects.filter(work=work)
        serializer = ArtisanSerializer(artisans, many=True)
        return Response(serializer.data)

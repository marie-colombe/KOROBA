from rest_framework import viewsets
from customer.models.customer_model import CustomerModel
from customer.serializers.customer_serializer import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        """Surcharge de la méthode create pour hacher le mot de passe avant de sauvegarder"""
        password = serializer.validated_data.pop('password', None)
        customer = serializer.save()
        if password:
            customer.set_password(password)
            customer.save() 

    def perform_update(self, serializer):
        """Surcharge de la méthode update pour gérer la mise à jour du mot de passe"""
        password = serializer.validated_data.pop('password', None)
        customer = serializer.save() 
        if password:
            customer.set_password(password)
            customer.save()

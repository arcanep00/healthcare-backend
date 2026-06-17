from rest_framework import serializers
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):

    serializer_class = PatientSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return Patient.objects.filter(
            created_by=self.request.user
        )
    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user
        )


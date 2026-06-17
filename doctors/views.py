from .serializers import DoctorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from .models import Doctor

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer

    permission_classes = [
        IsAuthenticated
    ]

    filter_backends = [
        SearchFilter,
        OrderingFilter
    ]

    search_fields = (
        "name",
        "specialization"
    )

    ordering_fields = [
        "name",
        "experience",
        "created_at"
    ]
from doctors.models import Doctor
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, MappingReadSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class PatientDoctorMappingView(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()

    serializer_class = PatientDoctorMappingSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return (
            PatientDoctorMapping.objects.filter(
                patient__created_by=self.request.user
            ).select_related(
                "patient",
                "doctor"
            )
        )

    def get_serializer_class(self):
        if self.action in [
            "list",
            "retrieve"
        ]:
            return MappingReadSerializer
        return PatientDoctorMappingSerializer

    @action(
        detail=False,
        methods=["get"],
        url_path=r"patient/(?P<patient_id>[^/.]+)"
    )
    

    def patient_doctors(self, request, patient_id=None):
        mappings = (
            self.get_queryset().filter(patient_id=patient_id)
        )
        doctors = []

        for mapping in mappings:
            doctors.append({
                "id": mapping.doctor.id,
                "name": mapping.doctor.name,
                "specialization": mapping.doctor.specialization
            })

        return Response(
            {
                "patient_id": patient_id,
                "doctors": doctors
            }
        )


























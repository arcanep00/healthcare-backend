from rest_framework import serializers
from .models import PatientDoctorMapping

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = [
            "id",
            "assigned_at"
        ]

    def validate(self, attrs):
        patient = attrs.get("patient")
        doctor = attrs.get("doctor")

        exists = (
            PatientDoctorMapping.objects.filter(
                patient=patient,
                doctor=doctor
            ).exists()
        )

        if exists:
            raise serializers.ValidationError(
                "Doctor already assigned to this patient"
            )
        return attrs

# Read Serializer -

class MappingReadSerializer(serializers.ModelSerializer):

    patient_name = serializers.CharField(
        source="patient.name",
        read_only=True
    )

    doctor_name = serializers.CharField(
        source="doctor.name",
        read_only=True
    )

    class Meta:
        model = PatientDoctorMapping

        fields = [
            "id",
            "patient",
            "patient_name",
            "doctor",
            "doctor_name",
            "assigned_at"
        ]


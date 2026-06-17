from .models import Doctor
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

        read_only_fields = [
            "id",
            "created_at",
            "updated_at"
        ]

    def validate_experience(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Experience cannot be negative"
            )
        return value

    def validate_phone(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Invalid phone number"
            )
        return value

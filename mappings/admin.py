from django.contrib import admin
from .models import PatientDoctorMapping

# Register your models here.
@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('id',)
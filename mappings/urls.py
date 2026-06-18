from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PatientDoctorMappingView

router = DefaultRouter()

router.register(
    "",
    PatientDoctorMappingView,
    basename="mappings"
)

urlpatterns = router.urls
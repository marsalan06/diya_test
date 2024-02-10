from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AppointmentViewSet, CounsellorViewSet, PatientViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'counsellors', CounsellorViewSet, basename='counsellor')
router.register(r'appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Appointment, Counsellor, Patient
from .serializers import (AppointmentSerializer, CounsellorSerializer,
                          PatientSerializer)


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(is_active=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK)


class CounsellorViewSet(viewsets.ModelViewSet):
    serializer_class = CounsellorSerializer

    def get_queryset(self):
        return Counsellor.objects.filter(is_active=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK)


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.filter(is_active=True)
        patient_id = self.request.query_params.get('patient_id')
        counsellor_id = self.request.query_params.get('counsellor_id')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if patient_id is not None:
            queryset = queryset.filter(patient__id=patient_id)
        if counsellor_id is not None:
            queryset = queryset.filter(counsellor__id=counsellor_id)
        if start_date and end_date:
            queryset = queryset.filter(appointment_date__range=[
                                       start_date, end_date])

        return queryset.order_by('-appointment_date')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK)

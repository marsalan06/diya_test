from rest_framework import serializers

from .models import Appointment, Counsellor, Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        # Check if both patient and counsellor are active
        if not data['patient'].is_active or not data['counsellor'].is_active:
            raise serializers.ValidationError(
                "Both patient and counsellor must be active to create an appointment.")

        # Check if the patient has any other active appointments
        if Appointment.objects.filter(patient=data['patient'], is_active=True).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError(
                "This patient already has an active appointment.")

        # Check if the counsellor has any other active appointments
        if Appointment.objects.filter(counsellor=data['counsellor'], is_active=True).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError(
                "This counsellor already has an active appointment.")

        return data

from django.contrib import admin

from .models import Appointment, Counsellor, Patient


class PatientAdmin(admin.ModelAdmin):
    # Columns shown in the admin list
    list_display = ('id', 'name', 'email', 'is_active')
    search_fields = ('name', 'email')  # Fields to search on in the admin


class CounsellorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_active')
    search_fields = ('name', 'email')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_patient_name', 'get_counsellor_name',
                    'appointment_date', 'is_active')
    search_fields = ('patient__name', 'counsellor__name', 'appointment_date')
    # Filter options on the side
    list_filter = ('is_active', 'appointment_date')

    def get_patient_name(self, obj):
        return obj.patient.name
    get_patient_name.admin_order_field = 'patient__name'  # Allows column order sorting
    get_patient_name.short_description = 'Patient Name'  # Renames column head

    def get_counsellor_name(self, obj):
        return obj.counsellor.name
    # Allows column order sorting
    get_counsellor_name.admin_order_field = 'counsellor__name'
    get_counsellor_name.short_description = 'Counsellor Name'  # Renames column head


# Register your models here with the custom admin classes
admin.site.register(Patient, PatientAdmin)
admin.site.register(Counsellor, CounsellorAdmin)
admin.site.register(Appointment, AppointmentAdmin)

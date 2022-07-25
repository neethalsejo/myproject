from django.contrib import admin

# Register your models here.
from .models import Hospital, Patient


class HospitalAdmin(admin.ModelAdmin):
    list_display = ['branch', 'slug', 'district', 'pediatrician', 'urologist', 'physician', 'gynaecologist', 'ent',
                    'description']
    prepopulated_fields = {'slug': ('branch',)}
    list_editable = ['description', 'pediatrician', 'urologist', 'physician', 'gynaecologist', 'ent']


admin.site.register(Hospital, HospitalAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ['username', 'pname', 'slug', 'age', 'gender', 'phone', 'email', 'branch', 'diseas', 'dname',
                    'appdate', 'bookeddate']
    prepopulated_fields = {'slug': ('pname',)}
    list_editable = ['branch', 'phone', 'dname', 'appdate']


admin.site.register(Patient, PatientAdmin)

# Register your models here.

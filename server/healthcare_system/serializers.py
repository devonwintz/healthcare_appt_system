from rest_framework import serializers
from .models import *


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'sex', 'dob', 'telephone', 'email', 'address_line_1',
                  'address_line_2', 'ward_village', 'city', 'country', 'created_by', 'created', 'updated_by', 'updated']

class DoctorSerializer(serializers.ModelSerializer):
    specialization = serializers.SlugRelatedField(
    many=True, 
    read_only=True,
    slug_field = "specialization_details"
    )

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialization', 'telephone', 'email',
                  'created_by', 'created', 'updated_by', 'updated']

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name', 'created_by', 'created', 'updated_by', 'updated']

class EmergencyContactSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
    many=True, 
    read_only=True,
    slug_field = "patient_details"
    )

    class Meta:
        model = Emergency_Contact
        fields = ['id', 'patient', 'first_name', 'last_name', 'relationship', 'telephone', 'email',
                  'created_by', 'created', 'updated_by', 'updated']

class AllergySerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
    many=False, 
    read_only=True,
    slug_field = "patient_details"
    )

    class Meta:
        model = Allergy
        fields = ['id', 'patient', 'name', 'symptom', 'medication',
                  'created_by', 'created', 'updated_by', 'updated']

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'start_time', 'end_time', 'status',
                  'created_by', 'created', 'updated_by', 'updated']

class AppointmentSerializer_(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
    many=False, 
    read_only=True,
    slug_field = "patient_details"
    )

    doctor = serializers.SlugRelatedField(
    many=False, 
    read_only=True,
    slug_field = "doctor_details"
    )


    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'start_time', 'end_time', 'status',
                  'created_by', 'created', 'updated_by', 'updated']



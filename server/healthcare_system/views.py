import json
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .publisher import Publisher
from .datetime_encoder import DatetimeEncoder
from rest_framework.permissions import IsAuthenticated


config = {'host': 'rabbitmq', 'port': 5672, 'queue': 'emailer'}

class PatientView(APIView):
    permission_classes = (IsAuthenticated,)
    @api_view(['GET', 'POST'])
    def patient_list(request, format=None):
        """
        Create a patient with the 'POST' method
        View all patients with the 'GET' method
        """

        if request.method == 'GET':
            # Get all patient records
            patients = Patient.objects.all()
            # Serialize the list of patient records
            serializer = PatientSerializer(patients, many=True)
            # Return the serialized patient data
            return Response(serializer.data)

        elif request.method == 'POST':
            # Serialize the post request data
            serializer = PatientSerializer(data=request.data)
            # Check if the data is valid and save if true
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'DELETE'])
    def patient_details(request, id, format=None):
        """
        Get a patient details with the 'GET' method
        Update a patient details with the 'PUT' method
        Delete a patient with the 'DELETE' method
        """

        try:
            patient = Patient.objects.get(pk=id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorView(APIView):
    permission_classes = (IsAuthenticated,)
    @api_view(['GET', 'POST'])
    def doctor_list(request, format=None):
        """
        Create a doctor with the 'POST' method
        View all doctors with the 'GET' method
        """

        if request.method == 'GET':
            # Get all doctors records
            doctors = Doctor.objects.all()
            # Serialize the list of doctor records
            serializer = DoctorSerializer(doctors, many=True)
            # Return the serialized doctor data
            return Response(serializer.data)

        elif request.method == 'POST':
            # Serialize the post request data
            serializer = DoctorSerializer(data=request.data)
            # Check if the data is valid and save if true
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'DELETE'])
    def doctor_details(request, id, format=None):
        """
        Get a doctor details with the 'GET' method
        Update a doctor details with the 'PUT' method
        Delete a doctor with the 'DELETE' method
        """

        try:
            doctor = Doctor.objects.get(pk=id)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = DoctorSerializer(doctor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            doctor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class SpecializationView(APIView):
    permission_classes = (IsAuthenticated,)
    @api_view(['GET', 'POST'])
    def specialization_list(request, format=None):
        """
        Create a speicalization with the 'POST' method
        View all speicalizations with the 'GET' method
        """

        if request.method == 'GET':
            # Get all speicalization records
            speicalizations = Specialization.objects.all()
            # Serialize the list of speicalization records
            serializer = SpecializationSerializer(speicalizations, many=True)
            # Return the serialized speicalization data
            return Response(serializer.data)

        elif request.method == 'POST':
            # Serialize the post request data
            serializer = SpecializationSerializer(data=request.data)
            # Check if the data is valid and save if true
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'DELETE'])
    def specialization_details(request, id, format=None):
        """
        Get a speicalization details with the 'GET' method
        Update a speicalization details with the 'PUT' method
        Delete a speicalization with the 'DELETE' method
        """

        try:
            speicalization = Specialization.objects.get(pk=id)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = SpecializationSerializer(speicalization)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = SpecializationSerializer(speicalization, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            speicalization.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class EmergencyContactView(APIView):
    permission_classes = (IsAuthenticated,)
    @api_view(['GET', 'POST'])
    def emergency_contact_list(request, format=None):
        """
        Create an emergency contact with the 'POST' method
        View all emergency contact  with the 'GET' method
        """

        if request.method == 'GET':
            # Get all emergency contact records
            emergency_contacts = Emergency_Contact.objects.all()
            # Serialize the list of emergency contact records
            serializer = EmergencyContactSerializer(emergency_contacts, many=True)
            # Return the serialized emergency contact data
            return Response(serializer.data)

        elif request.method == 'POST':
            # Serialize the post request data
            serializer = EmergencyContactSerializer(data=request.data)
            # Check if the data is valid and save if true
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'DELETE'])
    def emergency_contact_details(request, id, format=None):
        """
        Get an emergency contact details with the 'GET' method
        Update an emergency contact details with the 'PUT' method
        Delete an emergency contact with the 'DELETE' method
        """

        try:
            emergency_contact = Emergency_Contact.objects.get(pk=id)
        except Emergency_Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = EmergencyContactSerializer(emergency_contact)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = EmergencyContactSerializer(
                emergency_contact, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            emergency_contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class AllergyView(APIView):
    permission_classes = (IsAuthenticated,)
    @api_view(['GET', 'POST'])
    def allergy_list(request, format=None):
        """
        Create a allergy with the 'POST' method
        View all allergy with the 'GET' method
        """

        if request.method == 'GET':
            # Get all allergy records
            allergies = Allergy.objects.all()
            # Serialize the list of allergy records
            serializer = AllergySerializer(allergies, many=True)
            # Return the serialized allergy data
            return Response(serializer.data)

        elif request.method == 'POST':
            # Serialize the post request data
            serializer = AllergySerializer(data=request.data)
            # Check if the data is valid and save if true
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'DELETE'])
    def allergy_details(request, id, format=None):
        """
        Get an allergy details with the 'GET' method
        Update an allergy details with the 'PUT' method
        Delete an allergy with the 'DELETE' method
        """

        try:
            allergy = Allergy.objects.get(pk=id)
        except Allergy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = AllergySerializer(allergy)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = AllergySerializer(
                allergy, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            allergy.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentView(APIView):
    permission_classes = (IsAuthenticated,)
    @api_view(['GET', 'POST'])
    def appointment_list(request, format=None):
        """
        Create a appointment with the 'POST' method
        View all appointment with the 'GET' method
        """

        if request.method == 'GET':
            # Get all appointment records
            appointments = Appointment.objects.all()
            # Serialize the list of appoimment records
            serializer = AppointmentSerializer(appointments, many=True)
            # Return the serialized appointment data
            return Response(serializer.data)

        elif request.method == 'POST':
            # Serialize the post request data
            serializer = AppointmentSerializer(data=request.data)
            # Check if the data is valid and save if true
            if serializer.is_valid():
                appt = serializer.save()
                # Get the saved appointment record
                appointment = Appointment.objects.get(id=appt.id)
                # Serialize the appointment that contains additional properties
                serializer = AppointmentSerializer_(appointment)
                # Add message to emailer queue
                Publisher(config).publish('emailer', json.dumps(serializer.data, cls=DatetimeEncoder))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'DELETE'])
    def appointment_details(request, id, format=None):
        """
        Get an appointment details with the 'GET' method
        Update an appointment details with the 'PUT' method
        Delete an appointment with the 'DELETE' method
        """

        try:
            appointment = Appointment.objects.get(pk=id)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = AppointmentSerializer(
                appointment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

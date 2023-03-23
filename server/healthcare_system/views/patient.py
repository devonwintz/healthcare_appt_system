from ..models import *
from ..serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
        else:
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



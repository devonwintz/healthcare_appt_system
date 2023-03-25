from ..models import *
from ..serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
            serializer = DoctorSerializer_(doctors, many=True)
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
        else:
            if request.method == 'GET':
                serializer = DoctorSerializer_(doctor)
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

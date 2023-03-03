from ..models import *
from ..serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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

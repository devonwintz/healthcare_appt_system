from ..models import *
from ..serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
        except Specialization.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
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

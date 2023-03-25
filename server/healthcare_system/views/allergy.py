from ..models import *
from ..serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
            serializer = AllergySerializer_(allergies, many=True)
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
        else:
            if request.method == 'GET':
                serializer = AllergySerializer_(allergy)
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


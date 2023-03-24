import json
from ..models import *
from ..serializers import *
from ..publisher import Publisher
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..datetime_encoder import DatetimeEncoder
from rest_framework.permissions import IsAuthenticated

config = {'host': 'rabbitmq', 'port': 5672, 'queue': 'emailer'}

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
            serializer = AppointmentSerializer_(appointments, many=True)
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
                # Publisher(config).publish('emailer', json.dumps(serializer.data, cls=DatetimeEncoder))
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
        else:
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
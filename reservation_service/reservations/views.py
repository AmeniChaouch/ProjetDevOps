from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reservation
from .serializers import ReservationSerializer
from kafka.producer import send_reservation_event
class CreateReservationView(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()
            
            # Envoi de l'événement à Kafka
            send_reservation_event("reservation_created", {
                "salle_id": reservation.salle.id,
                "date_debut": str(reservation.date_debut),
                "date_fin": str(reservation.date_fin)
            })
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
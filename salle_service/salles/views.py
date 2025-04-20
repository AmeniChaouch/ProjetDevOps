from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Salle, Disponibilite
from .serializers import SalleSerializer, DisponibiliteSerializer

class SalleDisponibiliteView(generics.ListAPIView):
    serializer_class = SalleSerializer

    def get_queryset(self):
        salle_id = self.kwargs['salle_id']
        return Salle.objects.filter(id=salle_id).prefetch_related('disponibilites')
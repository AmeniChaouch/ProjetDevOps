
from rest_framework import serializers
from .models import Salle, Disponibilite

class DisponibiliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilite
        fields = ['id', 'salle', 'date_debut', 'date_fin', 'disponible']

class SalleSerializer(serializers.ModelSerializer):
    disponibilites = DisponibiliteSerializer(many=True, read_only=True)

    class Meta:
        model = Salle
        fields = ['id', 'nom', 'capacité', 'disponibilites']
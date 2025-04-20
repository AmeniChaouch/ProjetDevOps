# salle_service/kafka/consumer.py

from kafka import KafkaConsumer
import json
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "salle_service.settings")
django.setup()

from salles.models import Disponibilite, Salle

consumer = KafkaConsumer(
    'reservation_created',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='salle-service-group'
)

for message in consumer:
    data = message.value
    print(f"[Kafka] New reservation: {data}")
    
    salle_id = data["salle_id"]
    date_debut = data["date_debut"]
    date_fin = data["date_fin"]
    
    # Mise à jour : la plage horaire devient indisponible
    Disponibilite.objects.create(
        salle_id=salle_id,
        date_debut=date_debut,
        date_fin=date_fin,
        disponible=False
    )

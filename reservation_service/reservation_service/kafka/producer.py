from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_reservation_event(event_type, reservation_data):
    producer.send(event_type, reservation_data)
    producer.flush()
    

    
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

taxi_data = [{"location": "JFK", "hour": 9, "day": "Monday", "demand": 50}, ...] # Example data

for record in taxi_data:
    producer.send('taxi_data', record)
    time.sleep(1)

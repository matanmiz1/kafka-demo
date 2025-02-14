from kafka import KafkaProducer
from time import sleep
import os

KAFKA_SERVERS = os.environ['KAFKA_SERVERS']
TOPIC = os.environ['TOPIC']

if not KAFKA_SERVERS:
    raise ValueError("Missing env variable KAFKA_SERVERS")
if not TOPIC:
    raise ValueError("Missing env variable TOPIC")


print(f"Producing messages to topic {TOPIC}")

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVERS)

for i in range(1, 20):
    message = f'Event {i}'.encode()
    producer.send(TOPIC, value=message)
    sleep(2)

producer.flush()
producer.close()

print("Finished producing messages!")

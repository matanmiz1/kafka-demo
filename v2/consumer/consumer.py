from kafka import KafkaConsumer
from time import sleep
import os

KAFKA_SERVERS = os.environ['KAFKA_SERVERS']
TOPIC = os.environ['TOPIC']
GROUP = os.environ['GROUP']

if not KAFKA_SERVERS:
    raise ValueError("Missing env variable KAFKA_SERVERS")
if not TOPIC:
    raise ValueError("Missing env variable TOPIC")
if not GROUP:
    raise ValueError("Missing env variable GROUP")


print(f"Consuming messages from topic {TOPIC}!")

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_SERVERS,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=GROUP
)

while True:
    messages = consumer.poll(timeout_ms=3000)
    for topic_partition, messages in messages.items():
        for message in messages:
            print(message.value.decode())

consumer.close()

from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open("order_events.json", "r") as file:
    orders = json.load(file)
print(orders)
print(type(orders))

for order in orders:
    print(f"Sending order: {order['order_id']}")
    producer.send('order_details', value=order)
    time.sleep(2)  # Simulate time delay

producer.flush()
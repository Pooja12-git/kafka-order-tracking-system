from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'order_status_updates',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='notification_service_group'
)

print("Listening for order updates...")

for message in consumer:
    order = message.value
    print(f"Notification → Order {order['order_id']} is now {order['status']}")

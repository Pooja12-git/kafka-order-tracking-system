from kafka import KafkaConsumer, KafkaProducer
import json
import time

consumer = KafkaConsumer(
    'order_details',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='order_processor_group'
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

status_flow = ["PACKED", "SHIPPED", "DELIVERED"]

for message in consumer:
    order = message.value
    print(f"Processing order: {order['order_id']}")
    for status in status_flow:
        time.sleep(2)  # Simulate delay between steps
        order['status'] = status
        print(f"Updating status: {order['order_id']} -> {status}")
        producer.send('order_status_updates', value=order)

    producer.flush()

# 📦 Real-Time Order Tracking System using Kafka

This project demonstrates a real-time **order tracking system** built with **Apache Kafka** and **Python**, simulating an e-commerce-like workflow with Producers, Consumers, and Kafka topic pipelines.

---

## 🚀 Project Overview

The system simulates how orders flow through different stages — from placement to final delivery — using Kafka topics and Python microservices.

### 🔧 Files in the Project:

- ✅ `producer_order_details.py`: Reads new orders from a JSON file and sends them to the Kafka topic `order_details`
- ⚙️ `processor_order_status.py`: Listens to incoming orders, updates their status (`PACKED → SHIPPED → DELIVERED`), and sends updates to another topic `order_status_updates`
- 🔔 `consumer_notification_service.py`: Subscribes to the `order_status_updates` topic and prints real-time order notifications
- 📁 `order_events.json`: Sample data file with multiple new order entries

---

## 🛠️ Tech Stack

- Apache Kafka (local setup)
- Python (`kafka-python`)
- JSON for sample data
- No Docker, no dashboards — pure code-based simulation

---

## ▶️ How to Run

> Make sure your local Kafka and Zookeeper servers are running (default port `9092` for Kafka)

1. **Open 3 terminals and run the following in order:**


Terminal 1
python consumer_notification_service.py

Terminal 2
python processor_order_status.py

Terminal 3
python producer_order_details.py

import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()

# ===== MQTT Broker=====
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_USER = os.getenv("MQTT_USER")
MQTT_PASS = os.getenv("MQTT_PASS")

# ===== MQTT Client ======
CLIENT_ID = "warehouse_servo"
TOPIC_CMD = "warehouse/command"
TOPIC_STATUS = "warehouse/status"
TOPIC_CONNECTION = "warehouse/connection"

# ===== SERVO GPIO =====
PWM_GPIO=12
PI_GPIO=int(os.getenv("GPIO_PIN", "18"))

import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()

# ===== MQTT =====
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_USER = os.getenv("MQTT_USER")
MQTT_PASS = os.getenv("MQTT_PASS")

# ===== SERVO GPIO =====
PWM_GPIO=12
PI_GPIO=os.getenv("GPIO_PIN")

# ===== Topics ======
TOPIC_CMD = "warehouse/command"
TOPIC_STATUS = "warehouse/status"
TOPIC_CONNECTION = "warehouse/connection"
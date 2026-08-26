import paho.mqtt.client as mqtt

# ===== MQTT =====
MQTT_BROKER= "141.19.44.65"
MQTT_PORT= 18443
MQTT_USER="suedzucker"
MQTT_PASS="isomalt"

# ===== SERVO GPIO =====
PWM_GPIO=12
PI_GPIO=18

# ===== Topics ======
TOPIC_CMD = "warehouse/command"
TOPIC_STATUS = "warehouse/status"
TOPIC_CONNECTION = "warehouse/connection"
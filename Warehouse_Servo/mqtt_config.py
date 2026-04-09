import paho.mqtt.client as mqtt

# ===== MQTT =====
MQTT_BROKER= "141.19.44.65"
MQTT_PORT= 18443
MQTT_USER="suedzucker"
MQTT_PASS="isomalt"
#CLIENT_ID = "WebClient"

# ===== ROBOT =====
SERIAL_PORT="/dev/ttyAMA0"
BAUD=1000000

# ===== SERVO GPIO =====
PWM_GPIO=12

# ===== Topics ======
TOPIC_CMD = "warehouse/command"
TOPIC_STATUS = "warehouse/status"

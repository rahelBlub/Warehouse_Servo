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

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")
    client.subscribe(TOPIC_CMD)

def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()
    print(message.topic+" "+str(message.payload))


# ================= START =================

#client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)

client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT)

client.loop_start()

print("[Service] Warehouse Servo MQTT Service gestartet")

#while True:
#    client.publish(TOPIC_STATUS)

client.loop_stop()


def send_motor_command(topic, payload):
    print(f"Publishing to {topic}: {payload}")
    client.publish(topic, payload)

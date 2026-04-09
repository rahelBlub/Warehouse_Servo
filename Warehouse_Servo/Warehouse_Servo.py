from mqtt_config import *
from servo_skill import ServoSkill

servo = ServoSkill(PWM_GPIO, 50) # frequence = 50

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")
    client.subscribe(TOPIC_CMD)
    # starting with middle position
    servo.middle()

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

print("[Service] Warehouse Servo MQTT Service startet")

#while True:
#    client.publish(TOPIC_STATUS)

client.loop_stop()


def send_motor_command(topic, payload):
    print(f"Publishing to {topic}: {payload}")
    client.publish(topic, payload)

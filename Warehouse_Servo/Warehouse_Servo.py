import logging
import threading
import json
import time
from mqtt_config import *
from servo_skill import ServoSkill

servo = ServoSkill(PWM_GPIO, 50) # frequency = 50
skill_lock = threading.Lock()

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0 and client.is_connected():
        print("Connected to MQTT Broker!")
        client.subscribe(TOPIC_CMD)
        # client.subscribe("$SYS/#")
        time.sleep(1)
        servo.middle() # starting with middle position
    else:
        print(f'Failed to connect, return code {rc}')
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.


def on_disconnect(client, userdata, rc):
    logging.info("Disconnected with result code: %s", rc)
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        logging.info("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            logging.info("Reconnected successfully!")
            return
        except Exception as err:
            logging.error("%s. Reconnect failed. Retrying...", err)

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    logging.info("Reconnect failed after %s attempts. Exiting...", reconnect_count)

def send_motor_command(func, topic, payload):
    def wrapper():
        try:
            print(f"Publishing to {topic}: {payload}")
            client.publish(topic, payload)
            func()
        except Exception as e:
            client.publish(TOPIC_STATUS, json.dumps({
                "state": "error",
                "msg": str(e),
                "cmd": payload,
            }))
        finally:
            skill_lock.release()
    skill_lock.acquire()
    threading.Thread(target=wrapper).start()

def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()
    print(message.topic+" "+str(message.payload))

    if payload == "left":
        send_motor_command(servo.left(), TOPIC_CMD, payload)
    if payload == "right":
        send_motor_command(servo.right(), TOPIC_CMD, payload)


# ================= START =================

#client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)

client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect(MQTT_BROKER, MQTT_PORT)

client.loop_start()

print("[Service] Warehouse Servo MQTT Service startet")

#while True:
#    client.publish(TOPIC_STATUS)

try:
    while True:
        pass
finally:
    client.loop_stop()

import logging
import threading
import json
import time
from mqtt_config import *
from skills import Skillset

SERVO_FREQUENCY = 50
skill_lock = threading.Lock()
FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60


def on_connect(client, userdata, flags, rc):
    global servo
    if rc == 0 and client.is_connected():
        print("Connected to MQTT Broker!")
        logging.info("Connected to MQTT Broker!")
        client.subscribe(TOPIC_CMD)
        time.sleep(1)
        publish_connection_state({
            "state": "online",
            "online": True,
        })

    else:
        print(f'Failed to connect, return code {rc}')
        logging.info(f'Failed to connect, return code {rc}')
        publish_connection_state({
            "state": "offline",
            "online": False,
        })

def on_disconnect(client, userdata, rc):
    logging.info("Disconnected with result code: %s", rc)
    publish_connection_state({
        "state": "offline",
        "online": False,
    })
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        logging.info("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            logging.info("Reconnected successfully!")
            publish_connection_state({
                "state": "online",
                "online": True,
            })
            return
        except Exception as err:
            logging.error("%s. Reconnect failed. Retrying...", err)

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    logging.info("Reconnect failed after %s attempts. Exiting...", reconnect_count)

def publish_connection_state(payload):
    client.publish(TOPIC_CONNECTION, json.dumps(payload),retain=True)

def publish_status(state, message, payload):
    client.publish(TOPIC_STATUS, json.dumps({
                "state": state,
                "msg": message,
                "cmd": payload,
            }),retain=True)

def execute_command(topic, payload):
    print("execute command")

    try:
        print(f"Publishing to {topic}: {payload}")
        publish_status("operational", "working", payload)

        if payload == "left":
            servo.left()
        elif payload == "right":
            servo.right()
        elif payload == "middle":
            servo.middle()
        else:
            publish_status("error", "unknown command", payload)
            return

    except Exception as e:
        publish_status("error", str(e), payload)
    finally:
        skill_lock.release()


def on_message(client, userdata, message):
    print("message received")
    try:
        topic = message.topic
        payload = message.payload.decode()
        print(f"topic: {message.topic}, payload: {message.payload}, QoS={message.qos}")

        if skill_lock.locked():
            print("System busy")
            return

        skill_lock.acquire()

        threading.Thread(
            target=execute_command,
            args=(topic, payload)
        ).start()

    except Exception as e:
        publish_status("error", str(e), message.payload)



# ================= START =================

client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)

client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect(MQTT_BROKER, MQTT_PORT)
servo = Skillset(PI_GPIO)
client.loop_start()

print("[Service] Warehouse Servo MQTT Service")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\n[Service] Manuell beendet (Strg+C)")

finally:
    client.loop_stop()
    servo.close()

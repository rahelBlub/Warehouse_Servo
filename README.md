# Warehouse_Servo

Programm, welches einen Servo-Motor ansteuert und die Befehle per MQTT übermittelt.

## Aufbau

<u>Hardware aufbauen:</u>

1. Verbinde den Signal-PIN (gelb/orange) mit PIN 12 (GPIO 18)  
2. Verbinde den Ground-PIN (schwarz) mit GND  
3. Verbinde den VCC-PIN (rot) mit 5V - es wird empfohlen eine externe Stromversorgung zu verwenden, um Fluktuationen im Pi zu vermeiden.
4. Klonen des Repositories:

5. Start von pigpio daemon auf dem Pi: 

````bash
sudo pigpiod
````
6. Erstellen einer `.env`-Datei:

````python
MQTT_BROKER=
MQTT_PORT=
MQTT_USER=
MQTT_PASS=

GPIO_PIN=
````

7. Skript starten mit: 

````bash
python3 Warehouse_Servo.py
````

## MQTT

````python
TOPIC_CMD = "warehouse/command"
TOPIC_STATUS = "warehouse/status"
TOPIC_CONNECTION = "warehouse/connection"
````

| Übergabe-Wert (String) | Beschreibung |
|------------------------|---|
| right                  | Der Servo dreht sich auf ~120° mit einer Pulsbreite von 2000 ms. |
| left                   | Der Servo dreht sich auf ~60° mit einer Pulsbreite von 1000 ms. |
| middle                 | Der Servo bewegt sich auf 90° mit einer Pulsbreite von 1500 ms. |
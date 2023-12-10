import json
import paho.mqtt.client as mqtt
import time
import requests
from datetime import datetime

MQTT_SERVER = "167.172.86.42"
MQTT_PORT = 1883
MQTT_USERNAME = "ce_capstone"
MQTT_PASSWORD = "ce_capstone_2023"

MQTT_TOPIC_WATER_EC = "WaterStation/EC"
MQTT_TOPIC_WATER_PH = "WaterStation/PH"
MQTT_TOPIC_WATER_ORP = "WaterStation/ORP"
MQTT_TOPIC_WATER_TEMP = "WaterStation/TEMP"
MQTT_TOPIC_WATER_SALINITY = "WaterStation/SALINITY"

MQTT_TOPIC_SOIL_N = "SoilStation/N"
MQTT_TOPIC_SOIL_P = "SoilStation/P"
MQTT_TOPIC_SOIL_K = "SoilStation/K"
MQTT_TOPIC_SOIL_EC = "SoilStation/EC"
MQTT_TOPIC_SOIL_PH = "SoilStation/PH"
MQTT_TOPIC_SOIL_TEMP = "SoilStation/TEMP"
MQTT_TOPIC_SOIL_HUMID = "SoilStation/HUMID"

MQTT_TOPIC_AIR_LUX = "AirStation/LUX"
MQTT_TOPIC_AIR_TEMP = "AirStation/TEMP"
MQTT_TOPIC_AIR_HUMID = "AirStation/HUMID"
MQTT_TOPIC_AIR_NOISE = "AirStation/NOISE"
MQTT_TOPIC_AIR_PM2 = "AirStation/PM2.5"
MQTT_TOPIC_AIR_PM10 = "AirStation/PM10"
MQTT_TOPIC_AIR_ATMOSPHERE = "AirStation/ATMOSPHERE"


def mqtt_connected(client, userdata, flags, rc):

    print("Connected succesfully!!")

    client.subscribe(MQTT_TOPIC_WATER_EC)
    client.subscribe(MQTT_TOPIC_WATER_PH)
    client.subscribe(MQTT_TOPIC_WATER_ORP)
    client.subscribe(MQTT_TOPIC_WATER_TEMP)
    client.subscribe(MQTT_TOPIC_WATER_SALINITY)

    client.subscribe(MQTT_TOPIC_SOIL_N)
    client.subscribe(MQTT_TOPIC_SOIL_P)
    client.subscribe(MQTT_TOPIC_SOIL_K)
    client.subscribe(MQTT_TOPIC_SOIL_EC)
    client.subscribe(MQTT_TOPIC_SOIL_PH)
    client.subscribe(MQTT_TOPIC_SOIL_TEMP)
    client.subscribe(MQTT_TOPIC_SOIL_HUMID)

    client.subscribe(MQTT_TOPIC_AIR_LUX)
    client.subscribe(MQTT_TOPIC_AIR_TEMP)
    client.subscribe(MQTT_TOPIC_AIR_HUMID)
    client.subscribe(MQTT_TOPIC_AIR_NOISE)
    client.subscribe(MQTT_TOPIC_AIR_PM2)
    client.subscribe(MQTT_TOPIC_AIR_PM10)
    client.subscribe(MQTT_TOPIC_AIR_ATMOSPHERE)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")


def mqtt_recv_message(client, userdata, message):
    print(f"Received: --- Topic: {message.topic} - Value: {message.payload.decode('utf-8')}\n")


mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)

#Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.on_message = mqtt_recv_message

mqttClient.loop_start()
counter = 0

current_day = datetime.now().strftime("%Y-%m-%d")


while True:
    print("Client is running...", counter)
    value = requests.get("http://167.172.86.42:4000/api/v1/supabase/sensors")

    data = value.json()["data"]

    # print(data)
    for s in data:
        station_id = s["name"]
        sensors = s["current_value"]
        old_value = s["all_values"]
        if station_id == "SoilStation/EC":
            print("Time: ", s["created_at"])
            print("Id: ", s["name"])
            for s in old_value:
                # Ensure the fractional seconds part has at least 6 digits
                if len(s["created_at"]) < 32:
                    # Split the timestamp into the main part and the timezone offset
                    main_part, timezone_offset = s["created_at"].rsplit('+', 1)

                    # Ensure the fractional seconds part has at least 6 digits
                    # Ensure the fractional seconds part has exactly 6 digits
                    main_part_parts = main_part.split('.')
                    if len(main_part_parts) > 1:
                        main_part = f"{main_part_parts[0]}.{main_part_parts[1]:0<6}"

                    # Combine the main part and the timezone offset
                    new_timestamp_string = main_part + '+' + timezone_offset

                    s["created_at"] = new_timestamp_string

                try:
                    timestamp_object = datetime.fromisoformat(s["created_at"])
                    # Extract date and time components
                    Day = timestamp_object.strftime("%Y-%m-%d")

                    if current_day == datetime.fromisoformat(s["created_at"]).strftime("%Y-%m-%d"):
                        Time = datetime.fromisoformat(s["created_at"]).strftime("%H:%M")
                        print(f"Day: {Day} --- Time: {Time}")
                        print("Value: ", s["value"])
                        
                        print(f"Day: {Day} --- Time: {Time}")


                except ValueError as e:
                    print(f"Error: {e}")

    time.sleep(5) 
import paho.mqtt.client as mqtt
import serial
import time
from ReadUart import AnalyzeData

MQTT_SERVER = "178.128.28.238"
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

ser = serial.Serial(port = 'COM11', baudrate = 115200)

data = {'NodeID': 0, 'SensorID': 0, 'value': 0}

def mqtt_connected(client, userdata, flags, rc):
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
    print(f"\nReceived ---> Topic: {message.topic} - Value: {message.payload.decode('utf-8')}\n")

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)

#Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.on_message = mqtt_recv_message

mqttClient.loop_start()


while True:
    current_time = time.strftime("%H:%M:%S")

    line = ser.readline().decode('utf-8')
    AnalyzeData(line, data)

    print(f"\nPublish data to server ---> {data['NodeID']} - {data['SensorID']} - {data['value']}")

    if (data['NodeID'] == "WaterStation"):
        if (data['SensorID'] == "EC"):
            mqttClient.publish("WaterStation/EC", data['value'], retain=True)
            
        if (data['SensorID'] == "SALINITY"):
            mqttClient.publish("WaterStation/SALINITY", data['value'], retain=True)

        if (data['SensorID'] == "PH"):
            mqttClient.publish("WaterStation/PH", data['value'], retain=True)

        if (data['SensorID'] == "ORP"):
            mqttClient.publish("WaterStation/ORP", data['value'], retain=True)

        if (data['SensorID'] == "TEMP"):
            mqttClient.publish("WaterStation/TEMP", data['value'], retain=True)
            
    if (data['NodeID'] == "SoilStation"):
        if (data['SensorID'] == "TEMP"):
            mqttClient.publish("SoilStation/TEMP", data['value'], retain=True)

        if (data['SensorID'] == "HUMID"):
            mqttClient.publish("SoilStation/HUMID", data['value'], retain=True)

        if (data['SensorID'] == "EC"):
            mqttClient.publish("SoilStation/EC", data['value'], retain=True)

        if (data['SensorID'] == "PH"):
            mqttClient.publish("SoilStation/PH", data['value'], retain=True)

        if (data['SensorID'] == "N"):
            mqttClient.publish("SoilStation/N", data['value'], retain=True)

        if (data['SensorID'] == "P"):
            mqttClient.publish("SoilStation/P", data['value'], retain=True)

        if (data['SensorID'] == "K"):
            mqttClient.publish("SoilStation/K", data['value'], retain=True)

    if (data['NodeID'] == "AirStation"):
        if (data['SensorID'] == "TEMP"):
            mqttClient.publish("AirStation/TEMP", data['value'], retain=True)

        if (data['SensorID'] == "HUMID"):
            mqttClient.publish("AirStation/HUMID", data['value'], retain=True)

        if (data['SensorID'] == "LUX"):
            mqttClient.publish("AirStation/LUX", data['value'], retain=True)

        if (data['SensorID'] == "NOISE"):
            mqttClient.publish("AirStation/NOISE", data['value'], retain=True)

        if (data['SensorID'] == "PM2.5"):
            mqttClient.publish("AirStation/PM2.5", data['value'], retain=True)

        if (data['SensorID'] == "PM10"):
            mqttClient.publish("AirStation/PM10", data['value'], retain=True)

        if (data['SensorID'] == "ATMOSPHERE"):
            mqttClient.publish("AirStation/ATMOSPHERE", data['value'], retain=True)

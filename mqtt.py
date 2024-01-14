import paho.mqtt.client as mqtt

class MQTTHelper:

    MQTT_SERVER = "18.205.244.197"
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

    recvCallBack = None

    def mqtt_connected(self, client, userdata, flags, rc):

        print("Connected succesfully!!")

        client.subscribe(self.MQTT_TOPIC_WATER_EC)
        client.subscribe(self.MQTT_TOPIC_WATER_PH)
        client.subscribe(self.MQTT_TOPIC_WATER_ORP)
        client.subscribe(self.MQTT_TOPIC_WATER_TEMP)
        client.subscribe(self.MQTT_TOPIC_WATER_SALINITY)

        client.subscribe(self.MQTT_TOPIC_SOIL_N)
        client.subscribe(self.MQTT_TOPIC_SOIL_P)
        client.subscribe(self.MQTT_TOPIC_SOIL_K)
        client.subscribe(self.MQTT_TOPIC_SOIL_EC)
        client.subscribe(self.MQTT_TOPIC_SOIL_PH)
        client.subscribe(self.MQTT_TOPIC_SOIL_TEMP)
        client.subscribe(self.MQTT_TOPIC_SOIL_HUMID)

        client.subscribe(self.MQTT_TOPIC_AIR_LUX)
        client.subscribe(self.MQTT_TOPIC_AIR_TEMP)
        client.subscribe(self.MQTT_TOPIC_AIR_HUMID)
        client.subscribe(self.MQTT_TOPIC_AIR_NOISE)
        client.subscribe(self.MQTT_TOPIC_AIR_PM2)
        client.subscribe(self.MQTT_TOPIC_AIR_PM10)
        client.subscribe(self.MQTT_TOPIC_AIR_ATMOSPHERE)

    def mqtt_subscribed(self, client, userdata, mid, granted_qos):
        print("Subscribed to Topic!!!\n")

    def mqtt_recv_message(self, client, userdata, message):
        print(f"Received -----> Topic: {message.topic} ------ Value: {message.payload.decode('utf-8')}\n")
        self.recvCallBack(message)

    def __init__(self):

        self.mqttClient = mqtt.Client()
        self.mqttClient.username_pw_set(self.MQTT_USERNAME, self.MQTT_PASSWORD)
        self.mqttClient.connect(self.MQTT_SERVER, int(self.MQTT_PORT), 60)

        # Register mqtt events
        self.mqttClient.on_connect = self.mqtt_connected
        self.mqttClient.on_subscribe = self.mqtt_subscribed
        self.mqttClient.on_message = self.mqtt_recv_message

        self.mqttClient.loop_start()

    def setRecvCallBack(self, func):
        self.recvCallBack = func


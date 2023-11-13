// mqtt.service.ts
import { Injectable } from '@nestjs/common';
import * as mqtt from 'mqtt';
import { SupabaseService } from '../supabase/supabase.service';

@Injectable()
export class MqttService {
  private readonly MQTT_SERVER = 'mqttserver.tk';
  private readonly MQTT_PORT = 1883;
  private readonly MQTT_USERNAME = 'innovation';
  private readonly MQTT_PASSWORD = 'Innovation_RgPQAZoA5N';
  private readonly MQTT_TOPIC_SUB_SOIL = '/innovation/soilmonitoring';
  private readonly MQTT_TOPIC_SUB_WATER = '/innovation/watermonitoring';
  private readonly MQTT_TOPIC_SUB_AIR = '/innovation/airmonitoring';
  private readonly MQTT_TOPIC_SUB_VALVE = '/innovation/valvecontroller';
  private readonly MQTT_TOPIC_SUB_PUMP = '/innovation/pumpcontroller';
  // Add other MQTT topics as needed

  private mqttClient: mqtt.MqttClient;

  constructor(private readonly supabase: SupabaseService) {
    this.mqttClient = mqtt.connect(
      `mqtt://${this.MQTT_SERVER}:${this.MQTT_PORT}`,
      {
        username: this.MQTT_USERNAME,
        password: this.MQTT_PASSWORD,
      },
    );

    this.setupMqttHandlers();
  }

  private setupMqttHandlers() {
    this.mqttClient.on('connect', () => {
      console.log('Connected successfully!!');
      this.mqttClient.subscribe(this.MQTT_TOPIC_SUB_SOIL);
      this.mqttClient.subscribe(this.MQTT_TOPIC_SUB_WATER);
      this.mqttClient.subscribe(this.MQTT_TOPIC_SUB_AIR);
      this.mqttClient.subscribe(this.MQTT_TOPIC_SUB_VALVE);
      this.mqttClient.subscribe(this.MQTT_TOPIC_SUB_PUMP);
      // Subscribe to other topics here
    });

    this.mqttClient.on('message', async (topic, message) => {
      // Handle received messages
      console.log(`Received message on topic ${topic}: ${message.toString()}`);
      const temp = await this.supabase.getStationByName(
        JSON.parse(message.toString()).station_id,
      );
      console.log(temp);
    });
  }

  public setRecvCallBack(callback: (message: string) => void) {
    this.mqttClient.on('message', (_, message) => {
      callback(message.toString());
    });
  }
}

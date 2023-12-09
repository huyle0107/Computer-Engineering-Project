import { connect, MqttClient } from 'mqtt';
import { Injectable } from '@nestjs/common';
import { SupabaseService } from '../supabase/supabase.service';

@Injectable()
export class MqttService {
  private readonly client: MqttClient;

  constructor(private readonly supabase: SupabaseService) {
    // Replace 'mqtt://localhost:1883' with your MQTT server URL
    // Provide username and password in the options object

    this.client = connect('mqtt://167.172.86.42:1883', {
      username: 'ce_capstone',
      password: 'ce_capstone_2023',
    });

    // Handle connection events
    this.client.on('connect', () => {
      console.log('Connected to MQTT server');
      this.subscribeToTopics();
    });

    this.client.on('message', async (topic, message) => {
      console.log('Received message:', topic, message.toString());
      await this.supabase.insertSensorData({
        topic,
        message: message.toString(),
      });
    });

    this.client.on('error', (err) => {
      console.error('MQTT Error:', err);
    });
  }

  private subscribeToTopics() {
    // Define an array of topics to subscribe to
    const topicsToSubscribe = [
      'WaterStation/EC',
      'WaterStation/PH',
      'WaterStation/SALINITY',
      'WaterStation/TEMP',
      'WaterStation/ORP',
      'SoilStation/TEMP',
      'SoilStation/HUMID',
      'SoilStation/EC',
      'SoilStation/PH',
      'SoilStation/N',
      'SoilStation/P',
      'SoilStation/K',
      'AirStation/TEMP',
      'AirStation/HUMID',
      'AirStation/LUX',
      'AirStation/NOISE',
      'AirStation/PM2.5',
      'AirStation/PM10',
      'AirStation/ATMOSPHERE',
    ];

    // Subscribe to each topic
    topicsToSubscribe.forEach((topic) => {
      this.client.subscribe(topic, (err) => {
        if (!err) {
          console.log(`Subscribed to topic: ${topic}`);
        } else {
          console.error(`Error subscribing to topic ${topic}: ${err}`);
        }
      });
    });
  }
}

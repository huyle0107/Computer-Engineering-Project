// mqtt.service.ts
import { connect, MqttClient } from 'mqtt'; // Importing 'Client' as a type

import { Injectable } from '@nestjs/common';

@Injectable()
export class MqttService {
  private readonly client: MqttClient;

  constructor() {
    // Replace 'mqtt://localhost:1883' with your MQTT server URL
    // Provide username and password in the options object
    this.client = connect('mqtt://178.128.28.238:1883', {
      username: 'ce_capstone',
      password: 'ce_capstone_2023',
    });

    // Handle connection events
    this.client.on('connect', () => {
      console.log('Connected to MQTT server');
      // console.log(this.client);
    });

    this.client.on('message', (topic, message) => {
      console.log('Received message:', topic, message.toString());
    });

    this.client.on('error', (err) => {
      console.error('MQTT Error:', err);
    });
  }

  publish(topic: string, message: string): void {
    this.client.publish(topic, message);
  }

  subscribe(topic: string): void {
    this.client.subscribe(topic);
  }

  onMessage(callback: (topic: string, message: string) => void): void {
    this.client.on('message', (topic, message) => {
      callback(topic, message.toString());
    });
  }
}

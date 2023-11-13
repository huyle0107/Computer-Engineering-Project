import { Body, Controller, Post, Get } from '@nestjs/common';

import { MqttService } from './mqtt.service';

@Controller('mqtt')
export class MqttController {
  constructor(private readonly mqtt: MqttService) {}
  @Get('publish')
  publishMessage(): string {
    this.mqtt.publish('test_topic', 'Hello, MQTT from NestJS');
    return 'Message published from NestJS';
  }
}

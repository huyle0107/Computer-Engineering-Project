import { Body, Controller, Post, Get } from '@nestjs/common';

import { MqttService } from './mqtt.service';

@Controller('mqtt')
export class MqttController {
  constructor(private readonly mqtt: MqttService) {}
}

import {
  Controller,
  Post,
  UsePipes,
  ValidationPipe,
  Param,
  Body,
} from '@nestjs/common';

import { SensorsService } from './sensors.service';

@Controller('sensors')
export class SensorsController {
  constructor(private readonly sensorsService: SensorsService) {}

  @Post('create')
  @UsePipes(new ValidationPipe())
  async createSensor(@Body() data: any) {
    await this.sensorsService.insertSensor(data);
    return {};
  }
}

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

  @Post('watermonitoring/:id')
  @UsePipes(new ValidationPipe())
  async createSensor(@Param('id') sensorsType: string) {
    await this.sensorsService.insertSensor(sensorsType);
    return {};
  }
}

import {
  Controller,
  Post,
  UsePipes,
  ValidationPipe,
  Param,
  Body,
} from '@nestjs/common';

import { StationsService } from './stations.service';

@Controller('stations')
export class StationsController {
  constructor(private readonly stationsService: StationsService) {}

  @Post('create')
  @UsePipes(new ValidationPipe())
  async createStations(@Body() data: any) {
    await this.stationsService.insertStations(data);
    return {};
  }
}

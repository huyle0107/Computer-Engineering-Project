import { Inject, Injectable, Logger } from '@nestjs/common';
import { SupabaseClient } from '@supabase/supabase-js';
import { SupabaseService } from '../../library/supabase/supabase.service';

@Injectable()
export class SensorsService {
  private readonly logger = new Logger(SensorsService.name);
  constructor(
    // @Inject('SUPABASE_ADMIN') private readonly supabaseClient: SupabaseClient,
    private readonly supabase: SupabaseService,
  ) {}

  async insertSensor(data: any) {
    console.log(data);
    const station = await this.supabase.getStationByName(data.stationName);
    if (station.length === 0) return 'Station not found';

    data.stationId = station[0].id;

    return await this.supabase.insertSensors(data);
  }
}

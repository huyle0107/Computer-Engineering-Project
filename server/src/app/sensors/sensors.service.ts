import { Inject, Injectable, Logger } from '@nestjs/common';
import { SupabaseClient } from '@supabase/supabase-js';

@Injectable()
export class SensorsService {
  private readonly logger = new Logger(SensorsService.name);
  constructor(
    @Inject('SUPABASE_ADMIN') private readonly supabaseClient: SupabaseClient,
  ) {}

  async insertSensor(sensorsType: string) {
    return sensorsType;
  }
}

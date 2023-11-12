import { Inject, Injectable, Logger } from '@nestjs/common';
import { SupabaseClient } from '@supabase/supabase-js';

@Injectable()
export class StationsService {
  private readonly logger = new Logger(StationsService.name);
  constructor(
    @Inject('SUPABASE_ADMIN') private readonly supabaseClient: SupabaseClient,
  ) {}

  async insertStations(data) {
    console.log(data);
    return '';
  }
}

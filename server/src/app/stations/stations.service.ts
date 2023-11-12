import { Inject, Injectable, Logger } from '@nestjs/common';
import { SupabaseClient } from '@supabase/supabase-js';
import { SupabaseService } from '../../library/supabase/supabase.service';

@Injectable()
export class StationsService {
  private readonly logger = new Logger(StationsService.name);
  constructor(
    // @Inject('SUPABASE_ADMIN') private readonly supabaseClient: SupabaseClient,
    private readonly supabase: SupabaseService,
  ) {}

  async insertStations(data) {
    console.log(data);

    return await this.supabase.insertStations(data);
  }
}

import { Module } from '@nestjs/common';
import { SensorsController } from './sensors.controller';
import { SensorsService } from './sensors.service';
import { SupabaseModule } from '../../library/supabase/supabase.module';

@Module({
  imports: [SupabaseModule],
  controllers: [SensorsController],
  providers: [SensorsService],
})
export class SensorsModule {}

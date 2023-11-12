import { Module } from '@nestjs/common';
import { SupabaseModule } from 'src/library/supabase-admin/supabase-admin.module';
import { SensorsController } from './sensors.controller';
import { SensorsService } from './sensors.service';
@Module({
  imports: [SupabaseModule],
  controllers: [SensorsController],
  providers: [SensorsService],
})
export class SensorsModule {}

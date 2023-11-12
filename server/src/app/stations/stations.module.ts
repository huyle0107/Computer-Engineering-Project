import { Module } from '@nestjs/common';
import { StationsController } from './stations.controller';
import { StationsService } from './stations.service';
import { SupabaseModule } from '../../library/supabase/supabase.module';
@Module({
  imports: [SupabaseModule],
  controllers: [StationsController],
  providers: [StationsService],
})
export class StationsModule {}

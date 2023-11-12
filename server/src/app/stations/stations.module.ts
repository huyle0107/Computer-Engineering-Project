import { Module } from '@nestjs/common';
import { SupabaseModule } from 'src/library/supabase-admin/supabase-admin.module';
import { StationsController } from './stations.controller';
import { StationsService } from './stations.service';

@Module({
  imports: [SupabaseModule],
  controllers: [StationsController],
  providers: [StationsService],
})
export class StationsModule {}

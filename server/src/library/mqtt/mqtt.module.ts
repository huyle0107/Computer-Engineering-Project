import { Module } from '@nestjs/common';
import { MqttService } from './mqtt.service';
import { MqttController } from './mqtt.controller';
import { HttpModule } from '@nestjs/axios';
import { SupabaseModule } from '../supabase/supabase.module';

@Module({
  controllers: [MqttController],
  providers: [MqttService],
  imports: [HttpModule, SupabaseModule],
  exports: [MqttService],
})
export class MqttModule {}

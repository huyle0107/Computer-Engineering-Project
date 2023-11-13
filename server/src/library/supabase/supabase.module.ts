import { Module } from '@nestjs/common';
import { SupabaseService } from './supabase.service';
import { SupabaseController } from './supabase.controller';
import { HttpModule } from '@nestjs/axios';

@Module({
  controllers: [SupabaseController],
  providers: [SupabaseService],
  imports: [HttpModule],
  exports: [SupabaseService],
})
export class SupabaseModule {}

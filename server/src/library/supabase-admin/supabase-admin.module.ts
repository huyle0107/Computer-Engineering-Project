// supabase.module.ts
import { Module, Global } from '@nestjs/common';
import { createClient } from '@supabase/supabase-js';

@Global()
@Module({
  providers: [
    {
      provide: 'SUPABASE_ADMIN',
      useValue: createClient(
        process.env.SUPABASE_URL || 'https://rihnzkinhjnflusbkouv.supabase.co',
        process.env.SUPABASE_SERVICE_ROLE_KEY ||
          'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJpaG56a2luaGpuZmx1c2Jrb3V2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY4NjQwMjAsImV4cCI6MjAxMjQ0MDAyMH0.QXZo6W5cd_O9uLY_7cf6tRXETw-eYYscEJlRCqeoeZQ',
      ),
    },
  ],
  exports: ['SUPABASE_ADMIN'],
})
export class SupabaseModule {}

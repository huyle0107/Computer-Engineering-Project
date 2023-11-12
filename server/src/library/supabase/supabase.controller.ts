import { Body, Controller, Post, Get } from '@nestjs/common';

import { SupabaseService } from './supabase.service';

@Controller('supabase')
export class SupabaseController {
  constructor(private readonly supabase: SupabaseService) {}
}

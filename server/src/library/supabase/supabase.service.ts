import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';

import { SupabaseClient } from '@supabase/supabase-js';

@Injectable()
export class SupabaseService {
  private readonly supabaseUrl = this.configService.get('SUPABASE_URL');
  private readonly supabaseKey = this.configService.get('SUPABASE_KEY');
  private Supabase = require('@supabase/supabase-js');
  private supabaseClient: SupabaseClient;

  constructor(private readonly configService: ConfigService) {
    this.supabaseClient = this.Supabase.createClient(
      process.env.SUPABASE_URL || 'https://rihnzkinhjnflusbkouv.supabase.co',
      process.env.SUPABASE_SERVICE_ROLE_KEY ||
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJpaG56a2luaGpuZmx1c2Jrb3V2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY4NjQwMjAsImV4cCI6MjAxMjQ0MDAyMH0.QXZo6W5cd_O9uLY_7cf6tRXETw-eYYscEJlRCqeoeZQ',
    );
  }

  async insertStations(data) {
    const { data: res } = await this.supabaseClient
      .from('nodes')
      .insert(data)
      .select();

    return res;
  }

  async getStationByName(data) {
    const { data: res } = await this.supabaseClient
      .from('nodes')
      .select()
      .eq('name', data);

    return res;
  }

  async insertSensors(data) {
    console.log(data);
    for (const sensor of data.sensors) {
      await this.supabaseClient
        .from('sensors')
        .insert({
          name: sensor,
          node_id: data.stationId,
        })
        .select();
    }

    return '';
  }

  async insertSensorData(data: any) {
    try {
      await this.supabaseClient
        .from('sensors')
        .update({ current_value: data.message })
        .eq('name', data.topic)
        .select();

      const { data: sensorRes } = await this.supabaseClient
        .from('sensors')
        .select()
        .eq('name', data.topic);

      if (sensorRes.length > 0)
        await this.supabaseClient
          .from('sensor_output')
          .insert({
            sensor_id: sensorRes[0].id,
            value: data.message,
          })
          .select();
    } catch (e) {
      console.log(e.message);
    }
  }

  async getSensorData() {
    const dataRes = [];
    const { data: resSensors } = await this.supabaseClient
      .from('sensors')
      .select();
    for (const sensor of resSensors) {
      const { data: outputRes } = await this.supabaseClient
        .from('sensor_output')
        .select()
        .eq('sensor_id', sensor.id)
        .order('created_at', { ascending: false });

      sensor.all_values = outputRes || [];

      dataRes.push(sensor);
    }

    return { data: dataRes };
  }
}

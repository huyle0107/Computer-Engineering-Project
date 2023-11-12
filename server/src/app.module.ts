import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { AppController } from './app.controller';
import { AppService } from './app.service';

// import * as redisStore from 'cache-manager-redis-store';
// import { RedisService } from './lib/redis/redis.service';
import { ScheduleModule } from '@nestjs/schedule';
import { SensorsModule } from './app/sensors/sensors.module';
import { StationsModule } from './app/stations/stations.module';
import { MqttModule } from './library/mqtt/mqtt.module';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    // CacheModule.register({
    //   store: redisStore,
    //   host: 'redis-10767.c258.us-east-1-4.ec2.cloud.redislabs.com',
    //   port: 10767,
    //   // auth_pass: 'Vld0V1JWTldUbVpWUlVaVVZURmtVRlZyVVQwPQ',
    //   isGlobal: true,
    //   ttl: 30 * 24 * 60 * 60, //ttl  # 30 days * 24 hours * 60 minutes * 60 seconds
    // }),
    SensorsModule,
    StationsModule,
    MqttModule,
    ScheduleModule.forRoot(),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

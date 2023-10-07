import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { AppController } from './app.controller';
import { AppService } from './app.service';

// import * as redisStore from 'cache-manager-redis-store';
// import { RedisService } from './lib/redis/redis.service';
import { ScheduleModule } from '@nestjs/schedule';

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
    ScheduleModule.forRoot(),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

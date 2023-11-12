import { CACHE_MANAGER, Inject, Injectable } from '@nestjs/common';
import { Cache } from 'cache-manager';

@Injectable()
export class RedisService {
  constructor(@Inject(CACHE_MANAGER) private cacheManager: Cache) {}

  async get(key: string) {
    return await this.cacheManager.get(key);
  }

  async set(key: string, value: any, options?: { ttl: number }) {
    const ttl = options?.ttl;
    await this.cacheManager.set(key, value, { ttl });
  }

  async del(key: string) {
    await this.cacheManager.del(key);
  }
}

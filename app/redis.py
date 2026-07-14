# from redis import asyncio as aioredis
import redis.asyncio as redis
from app.settings import config

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

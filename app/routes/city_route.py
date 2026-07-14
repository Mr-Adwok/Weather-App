from fastapi import APIRouter
from ..settings import config
from app.services.service  import measure_execution_time
from app.redis import redis_client


import httpx
import json




weatherRouter = APIRouter()
weather_api_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"



@weatherRouter.get('/weather/{city}')
@measure_execution_time
async def get_city_info(city:str):
    url = f"{weather_api_url}/{city}?key={config.SECRET_KEY}"
    cache_key = f"weather:{city}"
     # Check if the data exists in cache
    cached_data = await redis_client.get(cache_key)
    if cached_data:
        print(cached_data)
        return {"source": "cache", "data": cached_data}

    async with httpx.AsyncClient() as conn:
        response = await conn.get(url)
        json_data = response.json()
        description = json_data['description']
        datetime = json_data.get('datetime')
        address = json_data.get('address')
        latitude = json_data.get('latitude');
        longitude = json_data.get('longitude')
        # print(response.status_code)
        result = {
            "address":address,
            "description":description,
            "datetime":datetime,
            "latitude":latitude,
            "longitude":longitude

        }
        dict_json = json.dumps(result)
        await redis_client.setex(cache_key,600,dict_json)


    # print(type(get_city_info,"Hello tere "))
    return {"response":result}



#  so you




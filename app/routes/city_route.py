from fastapi import APIRouter
from settings import config
import httpx



weatherRouter = APIRouter()
weather_api_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"



@weatherRouter.get('/weather/{city}')
async def get_city_info(city:str):
    url = f"{weather_api_url}/{city}?key={config.SECRET_KEY}"
    async with httpx.AsyncClient() as conn:
        response = await conn.get(url)
        json_data = response.json()
        description = json_data['description']
        datetime = json_data.get('datetime')
        address = json_data.get('address')
        latitude = json_data.get('latitude');
        longitude = json_data.get('longitude')

        print(response.status_code)


    # print(type(get_city_info,"Hello tere "))
    return {"response":{
        'address':address,
        'description':description,
        'datetime':datetime,
        'latitude':latitude,
        'longitude':longitude

    }}



#  so you




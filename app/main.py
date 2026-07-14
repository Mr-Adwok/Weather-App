# standart library

from fastapi import FastAPI





from app.schemas.schema import Input
from app.routes.city_route import weatherRouter
from app.services.service  import measure_execution_time

app = FastAPI()


@app.get('/')
@measure_execution_time
async def root():
    # print(WeatherRequestApp.requestNo,"Hello am number of requests")
    return {"message":'Hello world'}

@app.post('/ok')
async def Trail(input:Input):
    print(input)
    return {"Welcome to:": input}


print("hello error from here")
app.include_router(weatherRouter)
print("hello error from here")





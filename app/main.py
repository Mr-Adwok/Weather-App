from fastapi import FastAPI
from schemas.schema import Input
from routes.city_route import weatherRouter

app = FastAPI()


@app.get('/')
async def root():
    return {"message":'Hello world'}

@app.post('/ok')
async def Trail(input:Input):
    print(input)
    return {"Welcome to:": input}


print("hello error from here")
app.include_router(weatherRouter)
print("hello error from here")





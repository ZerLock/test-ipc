from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("health")
async def root():
    return {"message": "Je suis en vie"}


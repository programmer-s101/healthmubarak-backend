from fastapi import FastAPI
from app.routers import products

app = FastAPI()

@app.get("/")
def home():
    return {"message": "HealthMubarak Backend Running"}

app.include_router(products.router)

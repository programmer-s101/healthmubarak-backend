from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import products

app = FastAPI()

# ----------- Enable CORS (required for frontend to access backend) -----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "HealthMubarak Backend Running"}

# ----------- Routers -----------
app.include_router(products.router)

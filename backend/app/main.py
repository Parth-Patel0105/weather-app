from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class WeatherRequest(BaseModel):
    city: str


app = FastAPI(title="Weather App Backend")

# Enable CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Weather app backend"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/weather")
async def get_weather(req: WeatherRequest):
    # Placeholder implementation — replace with real API calls
    return {
        "city": req.city,
        "temperature_c": 20,
        "description": "Sunny",
    }

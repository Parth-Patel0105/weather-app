import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx


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
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENWEATHER_API_KEY not set on server")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": req.city, "appid": api_key, "units": "metric"}

    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.get(url, params=params)

    if resp.status_code != 200:
        # surface the error returned by OpenWeather
        raise HTTPException(status_code=resp.status_code, detail=resp.text)

    data = resp.json()
    return {
        "city": data.get("name"),
        "temperature_c": data.get("main", {}).get("temp"),
        "description": data.get("weather", [{}])[0].get("description"),
        "raw": data,
    }

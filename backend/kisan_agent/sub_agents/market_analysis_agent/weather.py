import requests
import json
from datetime import datetime

OPENWEATHER_API_KEY = "0b39c70be10e3a6f4329a2366e8d114d"

def weather_tool(location: str):
    """
    Returns a 10-day weather forecast for a given location (city or lat,lon).
    """

    try:
        # ✅ Step 1: Get coordinates if a city name is provided
        if "," not in location:
            geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={OPENWEATHER_API_KEY}"
            geo_res = requests.get(geo_url).json()
            if not geo_res:
                return f"Could not find location: {location}"
            latitude = geo_res[0]["lat"]
            longitude = geo_res[0]["lon"]
        else:
            latitude, longitude = map(float, location.split(","))

        # ✅ Step 2: Get forecast
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={OPENWEATHER_API_KEY}&units=metric"
        data = requests.get(url).json()

        if "list" not in data:
            return "Weather data unavailable."

        # ✅ Step 3: Aggregate daily forecast
        daily_forecast = {}
        for entry in data["list"]:
            date = entry["dt_txt"].split(" ")[0]
            temp = entry["main"]["temp"]
            rain = entry.get("rain", {}).get("3h", 0)
            weather = entry["weather"][0]["description"]

            if date not in daily_forecast:
                daily_forecast[date] = {"temps": [], "rain": 0, "conditions": []}

            daily_forecast[date]["temps"].append(temp)
            daily_forecast[date]["rain"] += rain
            daily_forecast[date]["conditions"].append(weather)

        forecast_summary = []
        for date, info in list(daily_forecast.items())[:10]:
            max_temp = round(max(info["temps"]), 1)
            min_temp = round(min(info["temps"]), 1)
            total_rain = round(info["rain"], 1)
            main_weather = max(set(info["conditions"]), key=info["conditions"].count)
            forecast_summary.append(
                f"{date}: {main_weather}, {min_temp}°C - {max_temp}°C, Rain: {total_rain}mm"
            )

        return "\n".join(forecast_summary)

    except Exception as e:
        return f"Error: {e}"

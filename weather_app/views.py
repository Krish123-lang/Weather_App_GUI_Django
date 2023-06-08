from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import requests
import json
from datetime import datetime
import pytz
import os


def home(request):
    api_key = os.environ.get("weather_api_key")
    base_url = "http://api.weatherapi.com/v1"

    # For current weather
    extension = '/current.json'
    place = request.POST.get("place")
    r = requests.get(f"{base_url}{extension}?key={api_key}&q={place}")

    data = r.json()
    time_obj = data['location']['localtime']

    lat, lon = data["location"]["lat"], data["location"]["lon"]
    condition = data["current"]["condition"]["text"]
    wind_mph, wind_kph = data["current"]["wind_mph"], data["current"]["wind_kph"]
    humidity = data["current"]["humidity"]

    messages.success(request, "Thank you for using this app !!! ")

    context = {
        "place": place,
        "locs": data['location']['tz_id'],
        "times": time_obj,
        "temps_c": data['current']['temp_c'],
        "temps_f": data['current']['temp_f'],
        "lat": lat,
        "lon": lon,
        "condition": condition,
        "wind_mph": wind_mph,
        "wind_kph": wind_kph,
        "humidity": humidity
    }
    return render(request, "home.html", context)

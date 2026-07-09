"""Functions for interacting with the OpenWeatherMap API"""

import requests

from config import API_KEY, BASE_URL


def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code == 200:
        return response.json()

    return None 
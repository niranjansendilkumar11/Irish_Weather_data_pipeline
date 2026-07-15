
import csv
import os
from datetime import datetime


def export_weather_to_csv(weather_records):

    os.makedirs("exports", exist_ok=True)

    filename = f"exports/weather_export_{datetime.now().strftime('%Y-%m-%d')}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "City",
            "Country",
            "Temperature",
            "Feels Like",
            "Humidity",
            "Pressure",
            "Wind Speed",
            "Weather",
            "Description"
        ])

        for weather in weather_records:

            writer.writerow([
                weather["city"],
                weather["country"],
                weather["temperature"],
                weather["feels_like"],
                weather["humidity"],
                weather["pressure"],
                weather["wind_speed"],
                weather["weather"],
                weather["description"]
            ])

    return filename
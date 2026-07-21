import csv
import os
from datetime import datetime


def export_weather_to_csv(weather_records,engineered_features):

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
            "Description",
            "Temperature Category",
            "Humidity Category",
            "Pressure Category",
            "Wind Category",
            "Weather Comfort",
            "Wind Intensity"
        ])

        for weather, feature in zip(weather_records, engineered_features):

            writer.writerow([
                weather["city"],
                weather["country"],
                weather["temperature"],
                weather["feels_like"],
                weather["humidity"],
                weather["pressure"],
                weather["wind_speed"],
                weather["weather"],
                weather["description"],
                feature["temperature_category"],
                feature["humidity_category"],
                feature["pressure_category"],
                feature["wind_category"],
                feature["weather_comfort"],
                feature["wind_intensity"]
            ])

    return filename
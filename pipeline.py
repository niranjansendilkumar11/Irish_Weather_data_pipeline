from config import IRISH_CITIES
from api import get_weather
from database import (
    create_connection,
    create_weather_table,
    insert_weather_data,
    fetch_all_weather,
    weather_record_exists
)
import logging
from utils import setup_logging


def main():

        setup_logging()

try:

    # Fetch weather for all configured Irish cities
    weather_records = []

    for city in IRISH_CITIES:

        weather = get_weather(city)

        if weather:
            weather_records.append(weather)
        else:
            logging.warning(f"Could not fetch weather for {city}")

    # Connect to SQLite database
    connection = create_connection()
    logging.info("Database connected successfully.")

    # Create table if it doesn't exist
    create_weather_table(connection)
    logging.info("weather_hourly table ready.")

    # Insert all weather records
    records_inserted = 0

    for weather in weather_records:

     if weather_record_exists(connection, weather["city"]):
        logging.info(f"Skipped {weather['city']} (already collected today)")
        continue

    insert_weather_data(connection, weather)
    records_inserted += 1

    logging.info("Weather data inserted successfully.")

    # Show total records in database
    rows = fetch_all_weather(connection)

    print(f"\nTotal records stored in database: {len(rows)}")

    connection.close()

    # Display current weather
    print("\nCurrent Weather Information")
    print("-" * 40)

    for weather in weather_records:

        print(f"\nCity         : {weather['city']}")
        print(f"Country      : {weather['country']}")
        print(f"Temperature  : {weather['temperature']} °C")
        print(f"Humidity     : {weather['humidity']} %")
        print(f"Pressure     : {weather['pressure']} hPa")
        print(f"Wind Speed   : {weather['wind_speed']} m/s")
        print(f"Weather      : {weather['description']}")

    print("\n" + "=" * 50)
    print("Weather Pipeline Completed Successfully")
    print("=" * 50)
    print(f"Cities Processed : {len(weather_records)}")
    print(f"Records Inserted : {records_inserted}")
    print("=" * 50)


    if __name__ == "__main__":
        main()

except Exception as error:

        logging.error(f"Pipeline failed: {error}")
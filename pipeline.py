import logging

from config import IRISH_CITIES
from api import get_weather
from database import (
    create_connection,
    create_weather_table,
    insert_weather_data,
    fetch_all_weather,
    weather_record_exists
)
from utils import setup_logging
from feature_engineering import generate_weather_features


def main():

    setup_logging()

    try:

        weather_records = []

        for city in IRISH_CITIES:

            weather = get_weather(city)

            if weather:
                weather_records.append(weather)

            else:
                logging.warning(f"Could not fetch weather for {city}")


        engineered_features = generate_weather_features(weather_records)

        print("\nEngineered Weather Features")
        print("-" * 40)

        for feature in engineered_features:

            print(f"\nCity                 : {feature['city']}")
            print(f"Country              : {feature['country']}")
            print(f"Temperature Category : {feature['temperature_category']}")
            print(f"Humidity Category    : {feature['humidity_category']}")
            print(f"Pressure Category    : {feature['pressure_category']}")
            print(f"Wind Category        : {feature['wind_category']}")


        connection = create_connection()
        logging.info("Database connected successfully.")

        create_weather_table(connection)
        logging.info("weather_hourly table ready.")

        records_inserted = 0

        for weather in weather_records:

            if weather_record_exists(connection, weather["city"]):
                logging.info(f"Skipped {weather['city']} (already collected today)")
                continue

            insert_weather_data(connection, weather)
            records_inserted += 1

        logging.info("Weather data inserted successfully.")

        rows = fetch_all_weather(connection)

        print(f"\nTotal records stored in database: {len(rows)}")

        connection.close()

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

    except Exception as error:

        logging.error(f"Pipeline failed: {error}")


if __name__ == "__main__":
    main()
import logging
import sqlite3

from config import IRISH_CITIES
from api import get_weather
from export import export_weather_to_csv
from database import (
    create_connection,
    create_weather_table,
    create_feature_table,
    insert_weather_data,
    insert_weather_feature,
    fetch_all_weather,
    weather_record_exists
)
from analytics import (
    get_average_temperature,
    get_highest_temperature,
    get_lowest_temperature,
    get_average_humidity,
    get_city_count,
    get_total_records,
    get_latest_collection_time
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
            print(f"Weather Comfort    : {feature['weather_comfort']}")
            print(f"Wind Intensity     : {feature['wind_intensity']}")


        connection = create_connection()
        logging.info("Database connected successfully.")

        create_weather_table(connection)
        logging.info("weather_hourly table ready.")

        create_feature_table(connection)
        logging.info("weather_features table ready.")

        records_inserted = 0
        features_inserted = 0

        for weather, feature in zip(weather_records, engineered_features):

            if weather_record_exists(connection, weather["city"]):
                logging.info(f"Skipped {weather['city']} (already collected today)")
                continue

            # Inserting raw weather
            insert_weather_data(connection, weather)
            records_inserted += 1

            # Inserting engineered features
            insert_weather_feature(connection, feature)
            features_inserted += 1

        logging.info("Weather data inserted successfully.")
        logging.info("Engineered weather features stored successfully.")

        stored_weather_records = fetch_all_weather(connection)

        print(f"\nTotal raw weather records stored: {len(stored_weather_records)}")

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
        print("\n" + "=" * 50)
        print("Weather Statistics")
        print("=" * 50)

        print(f"Unique Cities Stored  : {get_city_count(stored_weather_records)}")
        print(f"Total Records Stored  : {get_total_records(stored_weather_records)}")
        print(f"Average Temperature   : {get_average_temperature(stored_weather_records)} °C")
        print(f"Highest Temperature   : {get_highest_temperature(stored_weather_records)} °C")
        print(f"Lowest Temperature    : {get_lowest_temperature(stored_weather_records)} °C")
        print(f"Average Humidity      : {get_average_humidity(stored_weather_records)} %")
        print(f"Latest Collection     : {get_latest_collection_time(stored_weather_records)}")

        print("=" * 50)
        csv_file = export_weather_to_csv(weather_records)

        print(f"\nWeather data exported to: {csv_file}")

    except Exception as error:

        logging.error(f"Pipeline failed: {error}")


if __name__ == "__main__":
    main()
from config import IRISH_CITIES
from api import get_weather
from database import (
    create_connection,
    create_weather_table,
    insert_weather_data,
    fetch_all_weather
)


def main():

    # Fetch weather for Dublin
    weather = get_weather(IRISH_CITIES[0])

    # Connect to the database
    connection = create_connection()
    print("Database connected successfully.")

    # Create table
    create_weather_table(connection)
    print("weather_hourly table ready.")

    # Insert weather record
    insert_weather_data(connection, weather)
    print("Weather data inserted successfully.")

    # Display database contents
    rows = fetch_all_weather(connection)

    print("\nDatabase Contents")
    print("-" * 40)

    for row in rows:
        print(row)

    connection.close()

    # Display current weather
    print("\nCurrent Weather Information")
    print("-" * 40)

    for key, value in weather.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
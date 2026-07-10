from config import IRISH_CITIES
from api import get_weather
from database import create_connection


def main():

    weather = get_weather(IRISH_CITIES[0])

    connection = create_connection()

    print("Database connected successfully.")

    connection.close()

    print("\nCurrent Weather Information")
    print("-" * 30)

    for key, value in weather.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
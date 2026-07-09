from api import get_weather


def main():

    weather = get_weather("Dublin")

    if weather:

        print("City:", weather["name"])
        print("Temperature:", weather["main"]["temp"])
        print("Humidity:", weather["main"]["humidity"])
        print("Weather:", weather["weather"][0]["description"])


if __name__ == "__main__":
    main()
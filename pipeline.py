from api import get_weather


def main():

    print("Weather Data Pipeline\n")

    response = get_weather("Dublin")

    print("Status Code:", response.status_code)


if __name__ == "__main__":
    main()
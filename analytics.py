def get_average_temperature(weather_records):

    temperatures = [weather["temperature"] for weather in weather_records]

    return round(sum(temperatures) / len(temperatures), 2)


def get_highest_temperature(weather_records):

    temperatures = [weather["temperature"] for weather in weather_records]

    return max(temperatures)


def get_lowest_temperature(weather_records):

    temperatures = [weather["temperature"] for weather in weather_records]

    return min(temperatures)


def get_average_humidity(weather_records):

    humidity = [weather["humidity"] for weather in weather_records]

    return round(sum(humidity) / len(humidity), 2)


def get_city_count(weather_records):

    return len(weather_records)
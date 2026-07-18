def get_average_temperature(weather_records):
 

    temperatures = [record["temperature"] for record in weather_records]

    return round(sum(temperatures) / len(temperatures), 2)


def get_highest_temperature(weather_records):


    temperatures = [record["temperature"] for record in weather_records]

    return max(temperatures)


def get_lowest_temperature(weather_records):
  

    temperatures = [record["temperature"] for record in weather_records]

    return min(temperatures)


def get_average_humidity(weather_records):
 

    humidity = [record["humidity"] for record in weather_records]

    return round(sum(humidity) / len(humidity), 2)


def get_city_count(weather_records):
 

    cities = {record["city"] for record in weather_records}

    return len(cities)


def get_total_records(weather_records):
 
    return len(weather_records)


def get_latest_collection_time(weather_records):


    if not weather_records:
        return "No data available"

    latest_record = max(
        weather_records,
        key=lambda record: record["collected_at"]
    )

    return latest_record["collected_at"]
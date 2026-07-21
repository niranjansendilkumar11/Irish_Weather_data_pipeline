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

def get_average_temperature_by_city(weather_records):

    city_totals = {}
    city_counts = {}

    for record in weather_records:
        city = record["city"]

        city_totals[city] = city_totals.get(city, 0) + record["temperature"]
        city_counts[city] = city_counts.get(city, 0) + 1

    averages = {}

    for city in city_totals:
        averages[city] = round(city_totals[city] / city_counts[city], 2)

    return averages

def get_records_per_city(weather_records):

    city_records = {}

    for record in weather_records:
        city = record["city"]
        city_records[city] = city_records.get(city, 0) + 1

    return city_records

def get_latest_weather_record(weather_records):


    if not weather_records:
        return None

    return max(weather_records, key=lambda record: record["collected_at"])
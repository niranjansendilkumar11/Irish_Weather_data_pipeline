def categorize_temperature(temp):

    if temp < 5:
        return "Very Cold"

    elif temp < 10:
        return "Cold"

    elif temp < 20:
        return "Mild"

    elif temp < 30:
        return "Warm"

    return "Hot"


def categorize_humidity(humidity):

    if humidity < 40:
        return "Low"

    elif humidity < 70:
        return "Moderate"

    return "High"


def categorize_pressure(pressure):

    if pressure < 1000:
        return "Low"

    elif pressure <= 1020:
        return "Normal"

    return "High"


def categorize_wind_speed(speed):

    if speed < 3:
        return "Light"

    elif speed < 8:
        return "Moderate"

    return "Strong"


def categorize_weather_comfort(temp, humidity):

    if 15 <= temp <= 22 and 40 <= humidity <= 70:
        return "Comfortable"

    elif temp > 22 and humidity > 70:
        return "Uncomfortable"

    elif temp < 15:
        return "Uncomfortable"

    return "Moderate"


def categorize_wind_intensity(speed):

    if speed < 2:
        return "Calm"

    elif speed < 5:
        return "Breezy"

    return "Windy"


def generate_weather_features(weather_records):

    engineered_features = []

    for weather in weather_records:

        feature = {
            "city": weather["city"],
            "country": weather["country"],
            "temperature_category": categorize_temperature(weather["temperature"]),
            "humidity_category": categorize_humidity(weather["humidity"]),
            "pressure_category": categorize_pressure(weather["pressure"]),
            "wind_category": categorize_wind_speed(weather["wind_speed"]),

            # NEW FEATURES
            "weather_comfort": categorize_weather_comfort(
                weather["temperature"],
                weather["humidity"]
            ),

            "wind_intensity": categorize_wind_intensity(
                weather["wind_speed"]
            )
        }

        engineered_features.append(feature)

    return engineered_features
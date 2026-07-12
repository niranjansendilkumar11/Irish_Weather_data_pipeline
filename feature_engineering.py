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
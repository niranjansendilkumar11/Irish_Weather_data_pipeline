import unittest

from feature_engineering import (
    categorize_temperature,
    categorize_humidity,
    categorize_pressure,
    categorize_wind_speed
)


class TestFeatureEngineering(unittest.TestCase):

    def test_temperature_category(self):

        # Normal values
        self.assertEqual(categorize_temperature(2), "Very Cold")
        self.assertEqual(categorize_temperature(8), "Cold")
        self.assertEqual(categorize_temperature(15), "Mild")
        self.assertEqual(categorize_temperature(25), "Warm")
        self.assertEqual(categorize_temperature(35), "Hot")

        # Boundary values
        self.assertEqual(categorize_temperature(5), "Cold")
        self.assertEqual(categorize_temperature(10), "Mild")
        self.assertEqual(categorize_temperature(20), "Warm")
        self.assertEqual(categorize_temperature(30), "Hot")

    def test_humidity_category(self):

        self.assertEqual(categorize_humidity(20), "Low")
        self.assertEqual(categorize_humidity(55), "Moderate")
        self.assertEqual(categorize_humidity(90), "High")

        # Boundary values
        self.assertEqual(categorize_humidity(40), "Moderate")
        self.assertEqual(categorize_humidity(70), "High")

    def test_pressure_category(self):

        self.assertEqual(categorize_pressure(995), "Low")
        self.assertEqual(categorize_pressure(1015), "Normal")
        self.assertEqual(categorize_pressure(1030), "High")

        # Boundary values
        self.assertEqual(categorize_pressure(1000), "Normal")
        self.assertEqual(categorize_pressure(1020), "Normal")

    def test_wind_speed_category(self):

        self.assertEqual(categorize_wind_speed(2), "Light")
        self.assertEqual(categorize_wind_speed(5), "Moderate")
        self.assertEqual(categorize_wind_speed(10), "Strong")

        # Boundary values
        self.assertEqual(categorize_wind_speed(3), "Moderate")
        self.assertEqual(categorize_wind_speed(8), "Strong")


if __name__ == "__main__":
    unittest.main()
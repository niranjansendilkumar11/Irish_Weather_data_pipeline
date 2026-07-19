
import sqlite3
from config import DATABASE_PATH


def create_connection():
    
    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def create_weather_table(connection):
    

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_hourly (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            country TEXT NOT NULL,
            temperature REAL,
            feels_like REAL,
            humidity INTEGER,
            pressure INTEGER,
            wind_speed REAL,
            weather TEXT,
            description TEXT,
            collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()


def insert_weather_data(connection, weather):
    

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO weather_hourly (
            city,
            country,
            temperature,
            feels_like,
            humidity,
            pressure,
            wind_speed,
            weather,
            description
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        weather["city"],
        weather["country"],
        weather["temperature"],
        weather["feels_like"],
        weather["humidity"],
        weather["pressure"],
        weather["wind_speed"],
        weather["weather"],
        weather["description"]
    ))

    connection.commit()


def fetch_all_weather(connection):


    cursor = connection.cursor()

    cursor.execute("SELECT * FROM weather_hourly")

    return cursor.fetchall()

def weather_record_exists(connection, city):
    

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM weather_hourly
        WHERE city = ?
        AND collected_at >= datetime('now', '-30 minutes')
    """, (city,))

    count = cursor.fetchone()[0]

    return count > 0

def create_feature_table(connection):


    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_features (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            city TEXT,

            country TEXT,

            temperature_category TEXT,

            humidity_category TEXT,

            pressure_category TEXT,

            wind_category TEXT,
                   
            weather_comfort TEXT,
                   
            wind_intensity TEXT,

            collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

def insert_weather_feature(connection, feature):
    """
    Insert engineered weather features.
    """

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO weather_features (

            city,
            country,
            temperature_category,
            humidity_category,
            pressure_category,
            wind_category,
            weather_comfort,
            wind_intensity                   

        )

        VALUES (?, ?, ?, ?, ?, ?,?,?)
    """, (

        feature["city"],
        feature["country"],
        feature["temperature_category"],
        feature["humidity_category"],
        feature["pressure_category"],
        feature["wind_category"],
        feature["weather_comfort"],
        feature["wind_intensity"]

    ))

    connection.commit()
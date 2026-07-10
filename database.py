"""
Database functions for the Weather Data Pipeline.
"""

import sqlite3
from config import DATABASE_PATH


def create_connection():
    
    connection = sqlite3.connect(DATABASE_PATH)
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
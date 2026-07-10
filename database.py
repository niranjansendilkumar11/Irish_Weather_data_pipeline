"""Database connection for the Weather Data Pipeline."""

import sqlite3

from config import DATABASE_PATH


def create_connection():

    connection = sqlite3.connect(DATABASE_PATH)

    return connection
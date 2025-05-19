import psycopg2

from src.mp3_library.env import get_env


def get_db_connection():
    connection = psycopg2.connect(
        host=get_env("DB_HOST"),
        database=get_env("DB_NAME"),
        user=get_env("DB_USER"),
        password=get_env("DB_PASSWORD")
    )

    return connection

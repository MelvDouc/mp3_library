from flask import Flask, jsonify
from dotenv import dotenv_values
import psycopg2

app = Flask(__name__)

# Database connection setup


def get_db_connection():
    config = dotenv_values(".env.local")
    print("PRINT SHOULD BE HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(config)
    conn = psycopg2.connect(
        host=config["DB_HOST"],
        database=config["DB_NAME"],
        user=config["DB_USER"],
        password=config["DB_PASSWORD"]
    )

    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()

    if db_version is None:
        raise Exception("Could not retrieve DB version.")

    return jsonify({"PostgreSQL Version": db_version[0]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5173)

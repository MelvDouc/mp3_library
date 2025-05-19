from flask import Flask, make_response
from json import dumps as json_stringify

from src.mp3_library.routes import bp as views_bp
from src.mp3_library.routes.api import api_bp, url_prefix


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(views_bp)
    app.register_blueprint(api_bp, url_prefix=url_prefix)
    app.register_error_handler(Exception, handle_exception)
    return app


def handle_exception(e):
    response = make_response()
    response.data = json_stringify({
        "message": "Sorry, I must've messed up somewhere."
    })
    response.content_type = "application/json"
    return response


# Database connection setup


# @app.route('/')
# def index():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT version();')
#     db_version = cur.fetchone()
#     cur.close()
#     conn.close()

#     if db_version is None:
#         raise Exception("Could not retrieve DB version.")

#     return jsonify({"PostgreSQL Version": db_version[0]})

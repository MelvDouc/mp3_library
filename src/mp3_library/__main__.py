from src.mp3_library import create_app
from src.mp3_library.env import get_env

app = create_app()


if __name__ == "__main__":
    port = int(get_env("PORT"))
    app.run(host='0.0.0.0', port=port, debug=True)

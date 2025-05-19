""" Environment variables """

from dotenv import dotenv_values

__CONFIG = dotenv_values(".env.local")


def get_env(key: str) -> str:
    if not key in __CONFIG:
        raise Exception(f"'{key}' is not an environment variable.")

    return __CONFIG[key]  # type: ignore

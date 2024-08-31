import functools
import logging
from rest_framework.response import Response

logging.basicConfig(filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {name} : {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",)

def exception_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            logging.exception("Response Error")
            return Response({"error" : "something went wrong!"} , status=401)
    return wrapper
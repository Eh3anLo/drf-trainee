import logging
import json

from rest_framework.response import Response
from django.http import HttpResponse

logging.basicConfig(filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {name} : {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",)


class ExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    
    # def process_exception(self , request, exception):
    #     logging.exception("Response Error")
    #     return Response({"error" : "something went wrong!"} , status=401)
    


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            return view_func(request)
        except Exception:
            logging.exception("Response Error")
            response = HttpResponse(content=json.dumps({"error" : "something went wrong!"}) ,content_type='application/json')
            response.status_code = 401
            return response
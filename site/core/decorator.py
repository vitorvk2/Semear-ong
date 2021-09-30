from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.http import HttpRequest
from dataclasses import dataclass
from typing import Callable
import json


def has_data_body(function: Callable) -> Callable:
    def wrap(request: HttpRequest, *args, **kwargs):
        if request.method in ['POST', 'PUT', 'PATCH'] and request.body == b'':
            raise PermissionDenied

        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    
    return wrap


def validate_dataclass(dclass: Callable) -> Callable:
    def decorator(function: Callable):
        def wrap(request: HttpRequest, *args, **kwargs):
            try:
                data = json.loads(request.body)

                print(dclass)
                dclass(**data)

            except Exception:
                return JsonResponse(
                    {
                        'success': False,
                        'msg': 'Dadly formatted or not allowed fields'
                    },
                    status=422
                )

            return function(request, *args, **kwargs)

        wrap.__doc__ = function.__doc__
        wrap.__name__ = function.__name__
    
        return wrap
    return decorator
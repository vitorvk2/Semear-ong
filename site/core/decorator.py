from django.core.exceptions import PermissionDenied
from api.utils import check_password
from django.http import JsonResponse
from django.http import HttpRequest
from dataclasses import dataclass
from django.conf import settings
from typing import Callable
import json
import jwt


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


def is_authenticated(function: Callable) -> Callable:
    def wrap(request: HttpRequest, *args, **kwargs):
        token = request.COOKIES['token']
        validate = request.COOKIES['validate']

        try:
            data = jwt.decode(token, settings.JWT_KEY, algorithms=['HS256'])

        except:
            return JsonResponse(
                {
                    'success': False,
                    'msg': 'Forbidden'
                },
                status=403
            )

        if not check_password(validate, f"{data['id']}|{data['sym']}|{data['is_admin']}"):
            return JsonResponse(
                {
                    'success': False,
                    'msg': 'Forbidden'
                },
                status=403
            )

        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__

    return wrap
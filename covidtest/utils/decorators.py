import functools
import time
from copy import deepcopy
from functools import wraps

from django.core.exceptions import ValidationError
from django.db import connection, reset_queries
from rest_framework.response import Response
from rest_framework.status import is_success


def response_wrapper():
    """
    Decorator to make a view only accept request with required http method.
    :param required http method.
    """

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            response = func(request, *args, **kwargs)
            if response.data is not None:
                if "errors" not in response.data:
                    data = deepcopy(response.data)
                    if "notifications" in response.data:
                        notifications = data.pop("notifications")
                    else:
                        notifications = []
                    response.data = {
                        **{"success": True, "notifications": notifications},
                        **{"data": data},
                    }
                if "errors" in response.data:
                    if isinstance(response.data["errors"], dict):
                        for key in response.data["errors"]:
                            value = response.data["errors"][key]
                            if isinstance(value, list) and len(value) == 1:
                                response.data["errors"][key] = value[0]
            return response

        return inner

    return decorator


def except_data_error(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            return Response({"error": dict(e)})

    return func_wrapper


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.5f}s")
        return result

    return inner_func

import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rezult = func(*args, **kwargs)
        return json.dumps(rezult)
    return wrapper

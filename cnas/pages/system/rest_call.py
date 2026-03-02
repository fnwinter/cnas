"""rest_call annotation: Maps REST API path to method and stores it in page.rest_api_mapping."""


def rest_call(api_path: str):
    """Decorator that maps the given API path to the decorated method. Stored as {api_path: method_name} in page.rest_api_mapping."""

    def decorator(method):
        method._rest_api_path = api_path
        return method

    return decorator

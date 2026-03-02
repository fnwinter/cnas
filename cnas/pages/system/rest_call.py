"""rest_call annotation: REST API 경로와 메서드를 매핑해 page.rest_api_mapping에 보관합니다."""


def rest_call(api_path: str):
    """지정한 API 경로를 해당 메서드와 매핑하는 데코레이터. page.rest_api_mapping에 {api_path: method_name} 형태로 저장됩니다."""

    def decorator(method):
        method._rest_api_path = api_path
        return method

    return decorator

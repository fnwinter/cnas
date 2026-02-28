"""api_call annotation: POST 요청이 있으면 api_call() 반환값을 __str__ 결과로 사용합니다."""
from functools import wraps

from flask import request
from flask import has_app_context
from flask import has_request_context


def _has_post_data() -> bool:
    """REST API POST body가 있는지 확인."""
    if request.is_json:
        return True
    data = request.get_data(as_text=True)
    return bool(data and data.strip())


def api_call(method):
    """POST body가 있으면 self.api_call() 반환값을, 없으면 원래 __str__ 반환값을 사용하는 데코레이터."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if not has_request_context() or not has_app_context():
            return ""
        if request.method == "POST" and _has_post_data():
            if hasattr(self, "api_call") and callable(getattr(self, "api_call")):
                return self.api_call()
        return method(self, *args, **kwargs)

    return wrapper

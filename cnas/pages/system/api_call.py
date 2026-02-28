"""api_call annotation: POST 요청이 있으면 api_call() 결과를 self.api_result에 넣습니다 (pyscript처럼)."""
from functools import wraps

from flask import request
from flask import has_app_context
from flask import has_request_context

def api_call(method):
    """POST body가 있으면 self.api_call() 결과를 self.api_result에 넣고, 원래 __str__ 반환값을 그대로 반환합니다."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        print("api_call wrapper is called")
        if not hasattr(self, "api_result"):
            self.api_result = None
        print("api_call wrapper is called1")
        if request.method == "POST":
            print("api_call wrapper is called2")
            if hasattr(self, "post_api_call") and callable(getattr(self, "post_api_call")):
                print("api_call wrapper is called3")
                self.api_result = self.post_api_call()
                print("api_call wrapper is called4")
                return str(method(self, *args, **kwargs))
        print("api_call wrapper is called5")
        return str(method(self, *args, **kwargs))

    return wrapper
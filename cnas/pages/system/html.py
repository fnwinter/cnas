"""html annotation: 데코레이터로 지정한 파일 내용을 self.html에 주입합니다."""
import os
import sys
from functools import wraps


def html_file(filename: str):
    """지정한 파일 내용을 읽어 self.html에 넣은 뒤 원래 메서드를 실행하는 데코레이터."""

    def decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            cls = self.__class__
            module_name = cls.__module__
            if module_name not in sys.modules:
                raise RuntimeError(f"Module not loaded: {module_name}")
            module = sys.modules[module_name]
            module_path = getattr(module, "__file__", None)
            if not module_path:
                raise RuntimeError(f"Cannot resolve path for module: {module_name}")
            dir_path = os.path.dirname(os.path.abspath(module_path))
            file_path = os.path.join(dir_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                self.html = f.read()
            return method(self, *args, **kwargs)

        return wrapper

    return decorator

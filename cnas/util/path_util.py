import os

def rel_path(path, base_path, debug=False):
    """
    >>> from util.path_util import rel_path
    >>> rel_path("/abc/def/xyz/", "/abc/def", True)
    'xyz'
    >>> print(rel_path("/abc/def/xyz/", "/ab/cd", True))
    None
    >>> print(rel_path("/abc/def/xyz/", "/abc", True))
    def/xyz

    """
    if not os.path.exists(base_path) and debug is False:
        return None
    if not os.path.exists(path) and debug is False:
        return None
    _abs_path = os.path.abspath(path)
    _abs_base_path = os.path.abspath(base_path)
    _rel_path = os.path.relpath(_abs_path, _abs_base_path)
    if ".." in _rel_path:
        # wrong base path
        return None
    return _rel_path

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
    abs_path = os.path.abspath(path)
    abs_base_path = os.path.abspath(base_path)
    rel_path = os.path.relpath(abs_path, abs_base_path)
    if ".." in rel_path:
        # wrong base path
        return None
    return rel_path

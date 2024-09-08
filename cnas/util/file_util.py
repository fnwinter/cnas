import os

def is_image_file(_file):
    """
    Check whether the file is image file or not.

    >>> from util.file_util import is_image_file
    >>> is_image_file("test.jpg")
    True
    >>> is_image_file("test.png")
    True
    >>> is_image_file("test.PNG")
    True
    >>> is_image_file("test.doc")
    False

    """
    _, file_extension = os.path.splitext(_file)

    if file_extension.lower() in\
        [".jpg", ".png", ".webp", ".svg", ".bmp"]:
        return True
    return False

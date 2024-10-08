import os

from PIL import Image

from util.system_path import get_gallery_thumbnail_path
from util.config_path import get_gallery_path
from util.file_util import is_image_file

def correct_image_orientation(image):
    try:
        _exif = image.getexif()
        if _exif is None:
            return image

        ORIENTATION = "Orientation"
        _orientation = _exif.get(ORIENTATION)

        if _orientation == 3:
            image = image.rotate(180, expand=True)
        elif _orientation == 6:
            image = image.rotate(270, expand=True)
        elif _orientation == 8:
            image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError) as e:
        print(f"error while rotating tumbnail {e}")

    return image


def create_thumbnail(root_, rel_, file_, size=(256, 256)):
    full_path = os.path.join(*[root_, rel_, file_])

    thumb_ = get_gallery_thumbnail_path()

    full_thumb_ = os.path.join(thumb_, rel_)

    os.makedirs(full_thumb_, exist_ok=True)

    output_ = os.path.join(*[thumb_, rel_, file_])

    if os.path.exists(full_path):
        with Image.open(full_path) as img:
            img.thumbnail(size)
            img = correct_image_orientation(img)
            img.save(output_)


def generate_thumbnail():
    gallery_path = get_gallery_path()
    assert gallery_path, "No gallery root"
    for _root, _, files in os.walk(gallery_path):
        for _file in files:
            rel_path = os.path.relpath(_root, gallery_path)
            if is_image_file(_file):
                create_thumbnail(gallery_path, rel_path, _file)

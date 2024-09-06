import os
import threading
import time

from PIL import Image, ExifTags

from util.config import CONFIG
from util.system_path import get_gallery_thumbnail_path

def is_image_file(file_name):
    _, file_extension = os.path.splitext(file_name)
    if file_extension == '.png' or file_extension == '.jpg':
        return True
    return False

def correct_image_orientation(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = image._getexif()

        if exif and orientation in exif:
            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        pass

    return image


def create_thumbnail(root_folder, image_folder, file_path, size=(256, 256)):
    full_path = os.path.join(*[root_folder, image_folder, file_path])

    gallery_thumbnail_path = get_gallery_thumbnail_path()

    thumbnail_path = os.path.join(gallery_thumbnail_path, image_folder)

    os.makedirs(thumbnail_path, exist_ok=True)

    output_image_path = os.path.join(*[gallery_thumbnail_path, image_folder, file_path])

    if not os.path.exists(output_image_path):
        with Image.open(full_path) as img:
            img.thumbnail(size)
            img = correct_image_orientation(img)
            img.save(output_image_path)


def generate_thumbnail():
    gallery_root = CONFIG.get('gallery_path')
    assert gallery_root, "No gallery root"
    for file_root, _, files in os.walk(gallery_root):
        for _file in files:
            rel_path = os.path.relpath(gallery_root, file_root)
            if is_image_file(_file):
                create_thumbnail(file_root, rel_path, _file)

def background_task():
    while True:
        print("background service working...")
        generate_thumbnail()
        time.sleep(100)

def background():
    background_thread = threading.Thread(target=background_task)
    background_thread.daemon = True
    background_thread.start()

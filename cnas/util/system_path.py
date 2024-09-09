import os

def get_cnas_path():
    home_path = os.path.expanduser('~')
    config_path = os.path.join(home_path, ".cnas")

    if not os.path.exists(config_path):
      os.makedirs(config_path, exist_ok=True)
    return config_path

def get_gallery_path():
    return CONFIG.get("gallery_path")

def get_gallery_thumbnail_path():
    config_path = get_cnas_path()
    thumbnail_path = os.path.join(config_path, "gallery_thumbnail")
    if not os.path.exists(thumbnail_path):
        os.makedirs(thumbnail_path, exist_ok=True)
    return thumbnail_path

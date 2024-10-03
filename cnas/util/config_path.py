from util.config import CONFIG

def get_gallery_path():
    return CONFIG.get("gallery_path")

def get_music_path():
    return CONFIG.get("music_path")

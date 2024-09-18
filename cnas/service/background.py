import threading
import time

from service.thumbnail_service import generate_thumbnail

def background_task():
    while True:
        print("background service working...")
        generate_thumbnail()
        time.sleep(100)

def background():
    background_thread = threading.Thread(target=background_task)
    background_thread.daemon = True
    background_thread.start()

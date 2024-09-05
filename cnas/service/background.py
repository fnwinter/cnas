import threading
import time

def background_task():
    while True:
        print("background service working...")
        time.sleep(10)

def background():
    background_thread = threading.Thread(target=background_task)
    background_thread.daemon = True
    background_thread.start()

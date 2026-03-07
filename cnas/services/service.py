import multiprocessing
import time

from services.thumbnail import generate_thumbnail

def service_process_task():
    while True:
        print("service process working...")
        generate_thumbnail()
        time.sleep(100)


def service_process():
    background_process = multiprocessing.Process(target=service_process_task, daemon=True)
    background_process.start()

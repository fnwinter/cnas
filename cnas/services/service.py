import multiprocessing
from queue import Empty

from pages.base.system.cmd_message_queue import CmdMessageQueue
from services.command_handler import CmdHandler


def service_process_task(
    cmd_queue: multiprocessing.Queue,
    response_queue: multiprocessing.Queue,
) -> None:
    while True:
        while True:
            try:
                request_id, msg = cmd_queue.get(timeout=1.0)
                print("service_process_task event received:", msg)
                if response_queue is not None and request_id is not None:
                    result = CmdHandler.handle(msg)
                    response_queue.put((request_id, result))
            except Empty:
                break

def service_process() -> None:
    cmd_queue: multiprocessing.Queue = multiprocessing.Queue()
    response_queue: multiprocessing.Queue = multiprocessing.Queue()
    CmdMessageQueue.set_queues(cmd_queue, response_queue)
    background_process = multiprocessing.Process(
        target=service_process_task,
        args=(cmd_queue, response_queue),
        daemon=True,
    )
    background_process.start()

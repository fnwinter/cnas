"""Queue for sending commands/messages to the service process and receiving results."""

from __future__ import annotations

import multiprocessing
import threading
import uuid
from queue import Empty, Queue
from typing import Any


class CmdMessageQueue:
    """
    Request-response queue: main process sends messages to the service process
    and can wait for a result. Call set_queues() from the main process after
    creating the queues and before starting the service process.
    """

    _cmd_queue: multiprocessing.Queue | None = None
    _response_queue: multiprocessing.Queue | None = None
    _pending: dict[str, Queue] | None = None
    _lock: threading.Lock | None = None
    _reader_thread: threading.Thread | None = None

    @classmethod
    def set_queues(
        cls,
        cmd_queue: multiprocessing.Queue,
        response_queue: multiprocessing.Queue,
    ) -> None:
        """Set the shared queues and start the response reader thread."""
        cls._cmd_queue = cmd_queue
        cls._response_queue = response_queue
        cls._pending = {}
        cls._lock = threading.Lock()
        cls._reader_thread = threading.Thread(target=cls._response_reader_loop, daemon=True)
        cls._reader_thread.start()

    @classmethod
    def _response_reader_loop(cls) -> None:
        """Background thread: read (request_id, result) and dispatch to waiters."""
        while cls._response_queue is not None:
            try:
                request_id, result = cls._response_queue.get(timeout=1.0)
            except Empty:
                continue
            with cls._lock:
                waiter = cls._pending.pop(request_id, None)
            if waiter is not None:
                waiter.put(result)

    @classmethod
    def send_message(cls, message: Any, timeout: float = 10.0) -> Any | None:
        """
        Send a message to the service process and wait for the result.
        Returns the result from the service process, or None if queue not set or timeout.
        """
        if cls._cmd_queue is None or cls._response_queue is None or cls._pending is None:
            return None
        request_id = str(uuid.uuid4())
        waiter: Queue = Queue()
        with cls._lock:
            cls._pending[request_id] = waiter
        try:
            cls._cmd_queue.put((request_id, message))
            return waiter.get(timeout=timeout)
        except Empty:
            with cls._lock:
                cls._pending.pop(request_id, None)
            return None

    sendMessage = send_message

    @classmethod
    def put(cls, message: Any) -> bool:
        """Put a message without waiting for a response. Returns False if queues not set."""
        if cls._cmd_queue is None:
            return False
        cls._cmd_queue.put((None, message))
        return True

    @classmethod
    def get_nowait(cls) -> Any | None:
        """Get one message from cmd queue without blocking (for service process)."""
        if cls._cmd_queue is None:
            return None
        try:
            return cls._cmd_queue.get_nowait()
        except Empty:
            return None

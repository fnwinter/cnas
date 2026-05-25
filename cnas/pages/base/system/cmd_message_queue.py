"""Queue for sending commands/messages to the service process and receiving results."""

from __future__ import annotations

import multiprocessing
import threading
import uuid
from queue import Empty, Queue
from typing import Any


class _QueueState:
    def __init__(
        self,
        cmd_queue: multiprocessing.Queue,
        response_queue: multiprocessing.Queue,
    ) -> None:
        self.cmd_queue = cmd_queue
        self.response_queue = response_queue
        self.pending: dict[str, Queue] = {}
        self.lock = threading.Lock()


class CmdMessageQueue:
    """
    Request-response queue: main process sends messages to the service process
    and can wait for a result. Call set_queues() from the main process after
    creating the queues and before starting the service process.
    """

    _state: _QueueState | None = None
    _reader_thread: threading.Thread | None = None

    @classmethod
    def set_queues(
        cls,
        cmd_queue: multiprocessing.Queue,
        response_queue: multiprocessing.Queue,
    ) -> None:
        """Set the shared queues and start the response reader thread."""
        cls._state = _QueueState(cmd_queue, response_queue)
        cls._reader_thread = threading.Thread(target=cls._response_reader_loop, daemon=True)
        cls._reader_thread.start()

    @classmethod
    def _response_reader_loop(cls) -> None:
        """Background thread: read (request_id, result) and dispatch to waiters."""
        while True:
            state = cls._state
            if state is None:
                return
            try:
                request_id, result = state.response_queue.get(timeout=1.0)
            except Empty:
                continue
            with state.lock:
                waiter = state.pending.pop(request_id, None)
            if waiter is not None:
                waiter.put(result)

    @classmethod
    def send_message(cls, message: Any, timeout: float = 10.0) -> Any | None:
        """
        Send a message to the service process and wait for the result.
        Returns the result from the service process, or None if queue not set or timeout.
        """
        state = cls._state
        if state is None:
            return None
        request_id = str(uuid.uuid4())
        waiter: Queue = Queue()
        with state.lock:
            state.pending[request_id] = waiter
        try:
            state.cmd_queue.put((request_id, message))
            return waiter.get(timeout=timeout)
        except Empty:
            with state.lock:
                state.pending.pop(request_id, None)
            return None

    sendMessage = send_message

    @classmethod
    def put(cls, message: Any) -> bool:
        """Put a message without waiting for a response. Returns False if queues not set."""
        state = cls._state
        if state is None:
            return False
        state.cmd_queue.put((None, message))
        return True

    @classmethod
    def get_nowait(cls) -> Any | None:
        """Get one message from cmd queue without blocking (for service process)."""
        state = cls._state
        if state is None:
            return None
        try:
            return state.cmd_queue.get_nowait()
        except Empty:
            return None

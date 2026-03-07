"""Folder watcher that notifies when directory contents change."""

import logging
from pathlib import Path
from typing import Callable

from watchdog.events import (
    FileSystemEvent,
    FileSystemEventHandler,
    FileMovedEvent,
)
from watchdog.observers import Observer

logger = logging.getLogger(__name__)


class FolderWatcher:
    """
    Watches a directory and invokes callbacks on create, modify, delete, and move events.
    Runs the observer in a background thread. Call start() then stop() when done.
    """

    def __init__(
        self,
        watch_path: str | Path,
        on_created: Callable[[str], None] | None = None,
        on_modified: Callable[[str], None] | None = None,
        on_deleted: Callable[[str], None] | None = None,
        on_moved: Callable[[str, str], None] | None = None,
        recursive: bool = True,
    ) -> None:
        """
        Args:
            watch_path: Directory path to watch.
            on_created: Called with absolute path when a file/dir is created.
            on_modified: Called with absolute path when a file/dir is modified.
            on_deleted: Called with absolute path when a file/dir is deleted.
            on_moved: Called with (src_path, dest_path) when a file/dir is moved.
            recursive: If True, watch subdirectories as well.
        """
        self._watch_path = Path(watch_path).resolve()
        if not self._watch_path.is_dir():
            raise NotADirectoryError(f"watch_path must be a directory: {self._watch_path}")

        self._on_created = on_created
        self._on_modified = on_modified
        self._on_deleted = on_deleted
        self._on_moved = on_moved
        self._recursive = recursive
        self._observer = Observer()
        self._handler = _FolderEventHandler(self)

    def start(self) -> None:
        """Start watching in a background thread."""
        self._observer.schedule(
            self._handler,
            str(self._watch_path),
            recursive=self._recursive,
        )
        self._observer.start()
        logger.info("FolderWatcher started for %s (recursive=%s)", self._watch_path, self._recursive)

    def stop(self) -> None:
        """Stop the observer and wait for the thread to finish."""
        self._observer.stop()
        self._observer.join()
        logger.info("FolderWatcher stopped for %s", self._watch_path)

    def _dispatch_created(self, path: str) -> None:
        if self._on_created:
            try:
                self._on_created(path)
            except Exception as exc:
                logger.exception("on_created callback failed for %s: %s", path, exc)

    def _dispatch_modified(self, path: str) -> None:
        if self._on_modified:
            try:
                self._on_modified(path)
            except Exception as exc:
                logger.exception("on_modified callback failed for %s: %s", path, exc)

    def _dispatch_deleted(self, path: str) -> None:
        if self._on_deleted:
            try:
                self._on_deleted(path)
            except Exception as exc:
                logger.exception("on_deleted callback failed for %s: %s", path, exc)

    def _dispatch_moved(self, src_path: str, dest_path: str) -> None:
        if self._on_moved:
            try:
                self._on_moved(src_path, dest_path)
            except Exception as exc:
                logger.exception(
                    "on_moved callback failed for %s -> %s: %s",
                    src_path,
                    dest_path,
                    exc,
                )


class _FolderEventHandler(FileSystemEventHandler):
    """Internal handler that forwards watchdog events to FolderWatcher."""

    def __init__(self, watcher: FolderWatcher) -> None:
        super().__init__()
        self._watcher = watcher

    def _abs_path(self, event: FileSystemEvent) -> str:
        path = getattr(event, "dest_path", None) or event.src_path
        return str(Path(path).resolve())

    def on_created(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        self._watcher._dispatch_created(self._abs_path(event))

    def on_modified(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        self._watcher._dispatch_modified(self._abs_path(event))

    def on_deleted(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        self._watcher._dispatch_deleted(Path(event.src_path).resolve().as_posix())

    def on_moved(self, event: FileMovedEvent) -> None:
        if event.is_directory:
            return
        src = str(Path(event.src_path).resolve())
        dest = str(Path(event.dest_path).resolve())
        self._watcher._dispatch_moved(src, dest)

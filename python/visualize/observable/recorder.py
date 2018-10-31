from visualize.observable.observer import Observer
from queue import Queue


class Recorder(Observer):

    _queue: Queue
    _last_get_index: int
    _last_set_index: int

    def __init__(self) -> None:
        self._queue = Queue()
        self._last_get_index = None
        self._last_set_index = None

    def update(self, **kwargs) -> None:
        if kwargs["event"] == "get":
            if self._last_get_index is None:
                self._last_get_index = kwargs["key"]
            else:
                self._queue.put({"event": "compare", "m": self._last_get_index, "n": kwargs["key"], "state": kwargs["state"]})
                self._last_get_index = None
        if kwargs["event"] == "set":
            if self._last_set_index is None:
                self._last_set_index = kwargs["key"]
            else:
                self._queue.put({"event": "swap", "m": self._last_set_index, "n": kwargs["key"], "state": kwargs["state"]})
                self._last_set_index = None

    def empty(self):
        return self._queue.empty()

    def get(self):
        return self._queue.get()

    def __iter__(self):
        return self

    def __next__(self):
        if self._queue.empty():
            raise StopIteration
        return self._queue.get()

from queue import Queue
from typing import List


class ObservableArray:

    _event_queue: Queue
    _array: List
    index: int
    _m: int
    _n: int

    def __init__(self, *args):
        self._array = args[0]
        self.index = -1
        self._m = -1
        self._n = -1

    def set_queue(self, queue: Queue) -> None:
        self._event_queue = queue

    def copy(self) -> List:
        return self._array.copy()

    def __setitem__(self, key, value):
        if self._m == -1:
            self._m = key
        else:
            self._event_queue.put(("swap", self._array.copy(), self._m, key))
            self._m = -1
        self._array[key] = value

    def __len__(self):
        return len(self._array)

    def __getitem__(self, key: int):
        if self._n == -1:
            self._n = key
        else:
            self._event_queue.put(("compare", self._array.copy(), self._n, key))
            self._n = -1
        return self._array[key]

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index = self.index + 1
        if self.index > len(self._array) - 1:
            raise StopIteration
        return self._array[self.index]

    def __str__(self):
        return self._array.__str__()
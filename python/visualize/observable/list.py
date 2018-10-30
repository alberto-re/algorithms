from typing import List

from visualize.observable.observable import Observable


class ObservableList(Observable):
    _array: List
    _index: int

    def __init__(self, *args):
        super().__init__()
        self._array = args[0]

    def copy(self) -> List:
        return self._array.copy()

    def __setitem__(self, key: int, value):
        self._array[key] = value
        self.update(event="set", key=key, value=value, state=self._array.copy())

    def __len__(self):
        return len(self._array)

    def __getitem__(self, key: int):
        self.update(event="get", key=key, state=self._array.copy())
        return self._array[key]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self._array):
            raise StopIteration
        return self._array[self.index]

    def __str__(self):
        return str(self._array)

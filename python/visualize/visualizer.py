from queue import Queue
from tkinter import Tk, Canvas, mainloop
from typing import List
from random import randint

from algo.shuffling.fisher_yates import shuffle
from algo.sorting.selection_sort import sort


class Array:

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


class Display(Canvas):
    _interval: int
    _event_queue: Queue
    _array: List

    def __init__(self, width: int = 800, height: int = 600, interval: int = 200) -> None:
        super().__init__(width=width, height=height)
        self._interval = interval

    def run(self) -> None:
        self._draw_content()
        self.after(self._interval, self._update)
        self.pack()

    def set_queue(self, queue: Queue) -> None:
        self._event_queue = queue

    def set_array(self, array: List) -> None:
        self._array = array

    def _draw_content(self, event_type=None, m=None, n=None) -> None:

        start_x = 200
        y = 200
        width = 10
        height_unit = 10
        distance = 20

        base_color = "#576042"
        swap_color = "red"
        compare_color = "blue"

        for index, el in enumerate(self._array):
            x = start_x + index * distance
            fill_color = base_color
            if event_type == "swap" and (index == m or index == n):
                fill_color = swap_color
            if event_type == "compare" and (index == m or index == n):
                fill_color = compare_color
            self.create_rectangle(x, y, x + width, y + el * height_unit, fill=fill_color)

    def _update(self) -> None:
        if not self._event_queue.empty():
            self.delete("all")
            (event_type, array, m, n) = self._event_queue.get()
            self._array = array
            self._draw_content(event_type, m, n)
            self.after(self._interval, self._update)


def main() -> None:
    master = Tk()

    event_queue = Queue()

    array = [randint(1, 12) for _ in range(0, 20)]
    shuffle(array)
    array = Array(array)
    array.set_queue(event_queue)
    sort(array)

    canvas = Display()
    canvas.set_array(array)
    canvas.set_queue(event_queue)

    canvas.run()

    mainloop()


if __name__ == "__main__":
    main()

from tkinter import Canvas
from typing import List, Dict
from queue import Queue

COLORS = {
    "base": "#576042",
    "swap": "red",
    "compare": "blue"
}


class Board(Canvas):

    _interval: int
    _event_queue: Queue
    _array: List
    _initial_array: List
    _ops: Dict[int, List[int]]

    def __init__(self, width: int = 800, height: int = 600, interval: int = 100) -> None:
        super().__init__(width=width, height=height)
        self._interval = interval
        self._ops = {
            0: [0, 0],
            1: [0, 0]
        }

    def run(self) -> None:
        self._draw_initial()
        self._draw_content()
        self.after(self._interval, self._update)
        self.pack()

    def set_queue(self, queue: Queue) -> None:
        self._event_queue = queue

    def set_array(self, array: List) -> None:
        self._array = array
        self._initial_array = array.copy()

    def _draw_initial(self):
        self._draw_state(self._initial_array, 0)

    def _draw_content(self, event_type=None, m=None, n=None) -> None:
        self._draw_state(self._array, 1, event_type, m, n)

    def _draw_state(self, array, offset=0, event_type=None, m=None, n=None):

        start_x = 200
        y = 100 + (200 * offset)
        width = 10
        height_unit = 10
        distance = 20

        self.create_rectangle(start_x - 10, y - 20, start_x + 20 * len(array), y + 150)
        self.create_text(start_x - 5, y - 15, text="offset %d" % offset, anchor="nw")

        for index, el in enumerate(array):
            x = start_x + index * distance
            fill_color = COLORS["base"]
            if event_type == "swap" and (index == m or index == n):
                fill_color = COLORS["swap"]
                self._ops[offset][0] += 1
            if event_type == "compare" and (index == m or index == n):
                fill_color = COLORS["compare"]
                self._ops[offset][1] += 1
            self.create_rectangle(x, y + 140, x + width, y + 140 - (el * height_unit), fill=fill_color)

        if offset > 0:
            self.create_text((start_x + 20 * len(array)) - 105, y - 15, text="n. compares: %d" % self._ops[offset][1], anchor="ne")
            self.create_text((start_x + 20 * len(array)) - 15, y - 15, text="n. swap: %d" % self._ops[offset][0], anchor="ne")

    def _update(self) -> None:
        if not self._event_queue.empty():
            self.delete("all")
            (event_type, array, m, n) = self._event_queue.get()
            self._array = array
            self._draw_initial()
            self._draw_content(event_type, m, n)
            self.after(self._interval, self._update)
        else:
            self.delete("all")
            self._draw_initial()
            self._draw_content()
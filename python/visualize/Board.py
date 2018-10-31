from tkinter import Canvas
from typing import List, Dict
from visualize.observable.recorder import Recorder

COLORS = {
    "base": "#576042",
    "swap": "#ff0000",
    "compare": "#0099cc"
}


class Board(Canvas):

    _interval: int
    _recorder: List[Recorder]
    _initial_array: List = None
    _ops: Dict[int, List[int]]
    _last_events: List

    def __init__(self, width: int = 800, height: int = 600, interval: int = 100) -> None:
        super().__init__(width=width, height=height)
        self._interval = interval
        self._recorder = []
        self._last_events = []
        self._ops = {
            1: [0, 0],
            2: [0, 0]
        }

    def run(self) -> None:
        self.after(self._interval, self._update)
        self.pack()

    def add_recording(self, recorder: Recorder) -> None:
        self._recorder.append(recorder)
        self._last_events.append(None)

    def _draw_initial(self):
        self._draw_state(self._initial_array, 0)

    def _draw_content(self, index:int, array: List, event_type=None, m=None, n=None) -> None:
        self._draw_state(array, index, event_type, m, n)

    def _draw_state(self, array, offset=0, event_type=None, m=None, n=None):

        start_x = 40
        y = 40 + (200 * offset)
        width = 10
        height_unit = 10
        distance = 20

        self.create_rectangle(start_x - 10, y - 20, start_x + 20 * len(array), y + 150)
        self.create_text(start_x - 5, y - 15, text="offset %d" % offset, anchor="nw")

        if event_type == "swap":
            self._ops[offset][0] += 1
        if event_type == "compare":
            self._ops[offset][1] += 1

        for index, el in enumerate(array):
            x = start_x + index * distance
            fill_color = COLORS["base"]
            if event_type == "swap" and (index == m or index == n):
                fill_color = COLORS["swap"]
            if event_type == "compare" and (index == m or index == n):
                fill_color = COLORS["compare"]
            self.create_rectangle(x, y + 140, x + width, y + 140 - (el * height_unit), fill=fill_color)

        if offset > 0:
            self.create_text((start_x + 20 * len(array)) - 105, y - 15, text="n. compares: %d" % self._ops[offset][1], anchor="ne")
            self.create_text((start_x + 20 * len(array)) - 15, y - 15, text="n. swap: %d" % self._ops[offset][0], anchor="ne")

    def _update(self) -> None:
        self.delete("all")

        for index, recorder in enumerate(self._recorder):
            if not recorder.empty():
                event = recorder.get()
                self._last_events[index] = event
                array = event["state"]
                if self._initial_array is None:
                    self._initial_array = array.copy()
                self._draw_content(index+1, array, event["event"], event["m"], event["n"])
            else:
                event = self._last_events[index]
                array = event["state"]
                self._draw_content(index + 1, array)

        self._draw_initial()

        self.after(self._interval, self._update)

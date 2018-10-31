#!/usr/bin/env python

import optparse
from queue import Queue
from random import randint
from tkinter import Tk, mainloop

from algo.shuffling.fisher_yates import shuffle
from algo.sorting.bubble_sort import sort as bubble_sort
from algo.sorting.insertion_sort import sort as insertion_sort
from algo.sorting.merge_sort import sort as merge_sort
from algo.sorting.selection_sort import sort as selection_sort
from visualize.Board import Board
from visualize.observable.list import ObservableList
from visualize.observable.recorder import Recorder

ALGORITHMS = {
    "bubble_sort": bubble_sort,
    "merge_sort": merge_sort,
    "insertion_sort": insertion_sort,
    "selection_sort": selection_sort,
}

MIN_VAL = 1
MAX_VAL = 12


def parse_options():
    parser = optparse.OptionParser(usage="visualizer.py [OPTIONS]")
    parser.add_option("--length",
                      action="store", dest="length", default=25,
                      help="the length of the array (default 25)")
    parser.add_option("--interval",
                      action="store", dest="interval", default=200,
                      help="the interval in milliseconds between each refresh (default 20)")
    parser.add_option("--algorithm",
                      action="store", dest="algorithm", default="bubble_sort",
                      help="the algorithm to visualize (default 'bubble sort')")
    return parser.parse_args()


def main() -> None:
    (options, args) = parse_options()

    algoritms = options.algorithm.split(",")

    Tk()
    canvas = Board(interval=int(options.interval))

    initial_array = [randint(MIN_VAL, MAX_VAL) for _ in range(int(options.length))]
    shuffle(initial_array)

    for algorithm in algoritms:
        recorder = Recorder()
        array = ObservableList(initial_array.copy())
        array.register(recorder)
        ALGORITHMS[algorithm](array)
        canvas.add_recording(recorder)

    canvas.run()
    mainloop()


if __name__ == "__main__":
    main()

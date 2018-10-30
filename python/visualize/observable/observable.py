from abc import ABC

from visualize.observable.observer import Observer


class Observable(ABC):

    def __init__(self):
        self._observers: set = set()

    def register(self, observer: Observer) -> None:
        self._observers.add(observer)

    def update(self, **kwargs) -> None:
        for observer in self._observers:
            observer.update(**kwargs)

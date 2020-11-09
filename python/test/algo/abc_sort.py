import random
from abc import ABC, abstractmethod

import hypothesis.strategies as st
from hypothesis import given


class BaseSortTest(ABC):
    """A base class for all test cases on sorting algorithms

    This class doesn't inherit from unittest.TestCase to prevent
    the auto-loading by the unittest TestLoader.discover() method.
    """

    @abstractmethod
    def _sort(self, collection: list) -> list:
        pass  # Every subclass should define its own sorting strategy

    @given(st.lists(st.integers()))
    def test_correctness_against_python_impl(self, x: list) -> None:
        expected = sorted(x)
        self._sort(x)
        self.assertListEqual(expected, x)  # type: ignore  # see class docstring

    def test_correctness_against_python_impl_large_list(self) -> None:
        x = [random.randint(0, 500) for _ in range(1000)]
        expected = sorted(x)
        self._sort(x)
        self.assertListEqual(expected, x)  # type: ignore  # see class docstring

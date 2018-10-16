import unittest
from hypothesis import given
import hypothesis.strategies as st

from algo.sorting.bubble_sort import sort


class BubbleSortTest(unittest.TestCase):

    @given(st.lists(st.integers(), min_size=1, max_size=500))
    def test_correctness_against_python_impl(self, x):
        custom = sort(x)
        x.sort()
        self.assertEqual(x, custom)


if __name__ == '__main__':
    unittest.main()

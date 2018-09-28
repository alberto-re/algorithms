import random
import unittest

from algo.sorting.bubble_sort import sort


class BubbleSortTest(unittest.TestCase):

    def test_correctness_against_python_impl(self):
        for i in range(2, 200):
            items = [random.randint(-i, i) for _ in range(i)]
            custom = sort(items)
            items.sort()
            self.assertEqual(items, custom)


if __name__ == '__main__':
    unittest.main()

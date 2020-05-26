import unittest

from algo.sorting.merge_sort import merge_sort
from test.algo.abc_sort import BaseSortTest


class MergeSortTest(BaseSortTest, unittest.TestCase):

    def _sort(self, collection):
        return merge_sort(collection)


if __name__ == '__main__':
    unittest.main()

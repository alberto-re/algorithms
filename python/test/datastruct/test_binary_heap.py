import unittest
import random
from heapq import heappush, heappop

from datastruct.heap import BinaryHeap


class BinaryHeapTest(unittest.TestCase):

    def setUp(self):
        self.pq = BinaryHeap()

    def test_correctness_peek_from_empty(self):
        with self.assertRaises(IndexError):
            self.pq.peek()

    def test_correctness_pop_from_empty(self):
        with self.assertRaises(IndexError):
            self.pq.pop()

    def test_correctness_simple_case_1(self):
        self.pq.push(5)
        self.assertEqual(5, self.pq.peek())
        self.assertEqual(5, self.pq.pop())
        with self.assertRaises(IndexError):
            self.pq.pop()

    def test_correctness_simple_case_2(self):
        self.pq.push(1)
        self.pq.push(3)
        self.pq.push(5)
        self.assertEqual(5, self.pq.peek())
        self.assertEqual(5, self.pq.pop())
        self.assertEqual(3, self.pq.pop())
        self.assertEqual(1, self.pq.pop())

    def test_correctness_heapq_comparison(self):
        # See: heapq (https://docs.python.org/3.0/library/heapq.html)

        reference = []

        self.pq = BinaryHeap(lambda x, y: x < y)

        for _ in range(1000):
            random_item = random.randint(1, 500)
            self.pq.push(random_item)
            heappush(reference, random_item)

        for _ in range(1000):
            self.assertEqual(heappop(reference), self.pq.pop())


if __name__ == '__main__':
    unittest.main()

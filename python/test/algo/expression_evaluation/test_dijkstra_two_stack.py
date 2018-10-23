import unittest

from algo.expression_evaluation.dijkstra_two_stack import DijkstraTwoStackEvaluator


class DijkstraTwoStackTest(unittest.TestCase):

    def setUp(self):
        self.dts = DijkstraTwoStackEvaluator()

    def test_expr_1(self):
        self.assertEqual(23, self.dts.eval("( 2 + ( 14 + 7 ) )"))

    def test_expr_2(self):
        self.assertEqual(28, self.dts.eval("( 5 + ( ( 4 * 7 ) - ( 2 + 3 ) ) )"))


if __name__ == '__main__':
    unittest.main()

import random
import unittest

from algo.shuffling.fisher_yates import shuffle


class FisherYatesTest(unittest.TestCase):

    def test_shuffle_not_equals_before(self):
        items = [random.randint(0, 20) for _ in range(20)]
        shuffled = items.copy()
        shuffle(shuffled)
        self.assertNotEqual(items, shuffled)

    def test_probability_distribution(self):
        items = [1, 2, 3, 4, 5]

        distr = {}

        for itern in range(50000):
            shuffle(items)
            for index, item in enumerate(items):
                if itern == 0:
                    distr[item] = []
                distr[item].append(index)

        counts = {}
        for key, value in distr.items():
            if key not in counts:
                counts[key] = {}
            for i in value:
                if i not in counts[key]:
                    counts[key][i] = 1
                else:
                    counts[key][i] += 1

        for key in sorted(counts):
            probabilities = []
            tot = sum(counts[key].values())
            for val, n in counts[key].items():
                prob = n / tot
                probabilities.append(prob)
                self.assertAlmostEqual(0.2, prob, delta=0.01)


if __name__ == '__main__':
    unittest.main()

import sys
import random


def shuffle(items):
    for i in range(0, len(items)):
        rnd = random.randint(i, len(items) - 1)
        items[i], items[rnd] = items[rnd], items[i]


def main():
    items = [int(x) for x in sys.stdin.readline().split()]
    shuffle(items)
    print(" ".join(map(str, items)))


if __name__ == "__main__":
    main()
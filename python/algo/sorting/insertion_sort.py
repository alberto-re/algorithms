import sys


def insertion_sort(items: list) -> None:
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j - 1] > items[j]:
            items[j], items[j - 1] = items[j - 1], items[j]


def main() -> None:
    items = [int(x) for x in sys.stdin.readline().split()]
    insertion_sort(items)
    print(" ".join(map(str, items)))


if __name__ == "__main__":
    main()

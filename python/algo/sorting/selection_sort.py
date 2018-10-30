import sys


def sort(items: list) -> None:
    for i in range(0, len(items)):
        min_index = i
        for j in range(i, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]


def main() -> None:
    items = [int(x) for x in sys.stdin.readline().split()]
    sort(items)
    print(" ".join(map(str, items)))


if __name__ == "__main__":
    main()

import sys


def bubble_sort(items: list) -> None:
    while True:
        swapped = False
        for n in range(0, len(items) - 1):
            if items[n] > items[n + 1]:
                items[n], items[n + 1] = items[n + 1], items[n]
                swapped = True
        if not swapped:
            break

def main() -> None:
    items = [int(x) for x in sys.stdin.readline().split()]
    bubble_sort(items)
    print(" ".join(map(str, items)))


if __name__ == "__main__":
    main()

import sys


def sort(items: list) -> list:
    for m in range(0, len(items) - 1):
        for n in range(len(items) - 1, m, -1):
            if items[n] < items[n-1]:
                items[n], items[n-1] = items[n-1], items[n]
    return items


def main() -> None:
    items = [int(x) for x in sys.stdin.readline().split()]
    sort(items)
    print(" ".join(map(str, items)))


if __name__ == "__main__":
    main()

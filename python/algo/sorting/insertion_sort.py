import sys


def sort(items):
    for i in range(1, len(items)):
        for j in reversed(range(1, i)):
            if items[j] < items[j-1]:
                items[j], items[j-1] = items[j-1], items[j]
    return items


def main():
    items = [int(x) for x in sys.stdin.readline().split()]
    sort(items)
    print(" ".join(map(str, items)))


if __name__ == "__main__":
    main()

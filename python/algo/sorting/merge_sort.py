import sys


def _merge(array: list, lo: int, mid: int, hi: int) -> None:
    left = array[lo:mid+1]
    right = array[mid+1:hi+1]
    i, j = 0, 0
    k = lo
    for l in range(k, hi + 1):
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            array[l] = left[i]
            i += 1
        else:
            array[l] = right[j]
            j += 1


def _sort(array: list, lo: int, hi: int) -> None:
    if hi <= lo:
        return

    mid = (hi + lo) // 2
    _sort(array, lo, mid)
    _sort(array, mid+1, hi)
    _merge(array, lo, mid, hi)


def merge_sort(items: list) -> None:
    _sort(items, 0, len(items) - 1)


def main() -> None:
    items = [int(x) for x in sys.stdin.readline().split()]
    merge_sort(items)
    print(" ".join(map(str, items)))


if __name__ == "__main__":
    main()

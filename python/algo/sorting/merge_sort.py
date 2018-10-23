import sys


def merge(left: list, right: list) -> list:
    merged_items = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) or right_idx < len(right):
        if left_idx == len(left):
            merged_items.append(right[right_idx])
            right_idx += 1
        elif right_idx == len(right):
            merged_items.append(left[left_idx])
            left_idx += 1
        elif left[left_idx] <= right[right_idx]:
            merged_items.append(left[left_idx])
            left_idx += 1
        else:
            merged_items.append(right[right_idx])
            right_idx += 1
    return merged_items


def sort(items: list) -> list:
    if len(items) <= 1:
        return items
    else:
        center = len(items) - len(items) // 2
        return merge(sort(items[:center]), sort(items[center:]))


def main() -> None:
    items = [int(x) for x in sys.stdin.readline().split()]
    items = sort(items)
    print(" ".join(map(str, items)))


if __name__ == "__main__":
    main()

def bin_search(elems: list[int], target: int) -> bool:
    left, right = 0, len(elems) - 1

    while left <= right:
        middle = (right + left) // 2 # left + (right - left) // 2
        if elems[middle] == target:
            return True
        elif elems[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return False


def main() -> None:
    assert bin_search(sorted([1, 2, 5, 10, 1, 2, -5, 10, 11]), 1)
    assert bin_search(sorted([1, 2, 5, 10, 1, 2, -5, 10, 11]), 11)
    assert not bin_search(sorted([1, 2, 5, 10, 1, 2, -5, 10, 11]), 111)


if __name__ == "__main__":
    main()

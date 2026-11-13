def find(elems: list[int], target: int) -> bool:
    for elem in elems:
        if elem == target:
            return True
    return False


def main() -> None:
    assert find(sorted([1, 2, 5, 10, 1, 2, -5, 10, 11]), 1)
    assert find(sorted([1, 2, 5, 10, 1, 2, -5, 10, 11]), 11)
    assert not find(sorted([1, 2, 5, 10, 1, 2, -5, 10, 11]), 111)


if __name__ == "__main__":
    main()

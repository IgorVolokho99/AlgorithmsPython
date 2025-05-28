from typing import Any, TypeVar, Type

import pytest

from two_linked_list.two_linked_list import TwoLinkedList

E = TypeVar("E", bound=BaseException)


class TestMethodEq:
    @pytest.mark.parametrize(
        "initial_list_1, initial_list_2",
        [
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]),
            (["a", "b", "c"], ["a", "b", "c"]),
            (["a", 1, 2.0], ["a", 1, 2.0]),
            ([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]),
            ([], [])
        ]
    )
    def test_equal_lists(self, initial_list_1, initial_list_2):
        assert TwoLinkedList(initial_list_1) == TwoLinkedList(initial_list_2)

    @pytest.mark.parametrize(
        "initial_list_1, initial_list_2",
        [
            ([1, 2, 3], [1, 2, 4]),
            ([1, 2, 3], [1, 2, 3.0]),
            (["a"], [1]),
            ([1, 2, 3], []),
            ([], [1, 2, 3])
        ]
    )
    def test_not_equal_lists(self, initial_list_1, initial_list_2):
        assert TwoLinkedList(initial_list_1) != TwoLinkedList(initial_list_2)


class TestSet:
    # pytest tests/test_two_linked_list.py::TestSet
    @pytest.mark.parametrize(
        "two_linked_list, index, value, expected",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 0, 10, 10),
            (TwoLinkedList([1, 2, 3, 4, 5]), 4, 10, 10),
            (TwoLinkedList([1, 2, 3, 4, 5]), 2, 10, 10),
            (TwoLinkedList([1, 2, 3, 4, 5]), 2, "10", "10"),
            (TwoLinkedList([1, 2, 3, 4, 5]), 2, True, True)
        ]
    )
    def test_valid_args(self, two_linked_list: TwoLinkedList, index: int, value: Any, expected: Any) -> None:
        two_linked_list.set(index, value)
        assert two_linked_list.get(index) == expected

    @pytest.mark.parametrize(
        "two_linked_list, index, value, expected_exception",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 5.0, 10, TypeError),
            (TwoLinkedList([1, 2, 3, 4, 5]), "5.0", 10, TypeError),
            (TwoLinkedList([1, 2, 3, 4, 5]), True, 10, TypeError),
            (TwoLinkedList([1, 2, 3, 4, 5]), [], 10, TypeError),
            (TwoLinkedList([1, 2, 3, 4, 5]), -1, 10, ValueError),
            (TwoLinkedList([1, 2, 3, 4, 5]), -500, 10, ValueError),
            (TwoLinkedList([1, 2, 3, 4, 5]), 5, 10, IndexError),
            (TwoLinkedList([1, 2, 3, 4, 5]), 500, 10, IndexError)
        ]
    )
    def test_invalid_args(self, two_linked_list: TwoLinkedList, index: Any, value: Any,
                          expected_exception: Type[E] | tuple[Type[E], ...]) -> None:
        with pytest.raises(expected_exception):
            two_linked_list.set(index, value)


class TestReverseMethod:
    # pytest tests/test_two_linked_list.py::TestReverseMethod
    @pytest.mark.parametrize(
        "base_list, two_linked_list, expected",
        [
            (base_list := [1, 2, 3, 4, 5], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [1, 2, 3, 4], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [5, 5, 5, 5, 5], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [1, 2], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [1], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1]))
        ]
    )
    def test_simple_case(self, base_list: list, two_linked_list: TwoLinkedList, expected: TwoLinkedList) -> None:
        two_linked_list.reverse()
        assert two_linked_list == expected, f"Ошибка при аргументе: {base_list}"


class TestReversedMethod:
    # pytest tests/test_two_linked_list.py::TestReversedMethod
    @pytest.mark.parametrize(
        "base_list, two_linked_list, expected",
        [
            (base_list := [1, 2, 3, 4, 5], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [1, 2, 3, 4], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [1, 2], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [1], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1])),
            (base_list := [1, 2, "3", [4, 5], True], TwoLinkedList(base_list), TwoLinkedList(base_list[::-1]))
        ]
    )
    def test_simple_case(self, base_list: list, two_linked_list: TwoLinkedList, expected: TwoLinkedList):
        assert TwoLinkedList(reversed(two_linked_list)) == expected, f"Ошибка при аргументе: {base_list}"
# pytest tests/test_two_linked_list.py

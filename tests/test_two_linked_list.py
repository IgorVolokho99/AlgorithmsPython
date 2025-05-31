import copy
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


class TestClear:
    # pytest tests/test_two_linked_list.py::TestClear
    @pytest.mark.parametrize(
        "base_list, two_linked_list",
        [
            (base_list := [1, 2, 3, 4, 5], TwoLinkedList(base_list)),
            (base_list := [1, 2, 3, 4], TwoLinkedList(base_list)),
            (base_list := [1, 2], TwoLinkedList(base_list)),
            (base_list := [1], TwoLinkedList(base_list)),
            (base_list := [], TwoLinkedList(base_list)),
            (base_list := [1, 2.0, "3", [4, 4.0], True], TwoLinkedList(base_list))
        ]
    )
    def test_simple_case(self, base_list: list, two_linked_list: TwoLinkedList) -> None:
        two_linked_list.clear()
        assert two_linked_list.size() == 0, f"Ошибка при аргументе: {base_list}"


class TestExtend:
    # pytest tests/test_two_linked_list.py::TestExtend
    @pytest.mark.parametrize(
        "tll1, tll2, expected",
        [
            (TwoLinkedList([1, 2, 3]), TwoLinkedList([4, 5, 6]), TwoLinkedList([1, 2, 3, 4, 5, 6])),
            (TwoLinkedList([]), TwoLinkedList([4, 5, 6]), TwoLinkedList([4, 5, 6])),
            (TwoLinkedList([1, 2, 3]), TwoLinkedList([]), TwoLinkedList([1, 2, 3])),
            (TwoLinkedList([1]), TwoLinkedList([2]), TwoLinkedList([1, 2])),
            (TwoLinkedList([1]), TwoLinkedList([]), TwoLinkedList([1])),
            (TwoLinkedList([]), TwoLinkedList([1]), TwoLinkedList([1])),
            (TwoLinkedList(["Hello", 2, 3, 4, 5]), TwoLinkedList([2.0, [1, 2], True]),
             TwoLinkedList(["Hello", 2, 3, 4, 5, 2.0, [1, 2], True])),

        ]
    )
    def test_simple_case(self, tll1: TwoLinkedList, tll2: TwoLinkedList, expected: TwoLinkedList) -> None:
        tll1.extend(tll2)
        assert tll1 == expected


class TestIter:
    # pytest tests/test_two_linked_list.py::TestIter
    @pytest.mark.parametrize(
        "two_linked_list, expected",
        [
            (TwoLinkedList(base_list := [1, 2, 3, 4, 5]), base_list),
            (TwoLinkedList(base_list := [1, 2, 3, 4]), base_list),
            (TwoLinkedList(base_list := [1, 2]), base_list),
            (TwoLinkedList(base_list := [1]), base_list),
            (TwoLinkedList(base_list := []), base_list),
            (TwoLinkedList(base_list := [1, "Hello", 2.0, [3, 4, 5], True]), base_list)
        ]
    )
    def test_simple_case(self, two_linked_list: TwoLinkedList, expected: list) -> None:
        assert [value for value in two_linked_list] == expected, f"Ошибка при аргументе: {expected}"


class TestStr:
    # pytest tests/test_two_linked_list.py::TestStr
    @pytest.mark.parametrize(
        "two_linked_list, expected",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), "[1, 2, 3, 4, 5]"),
            (TwoLinkedList([1, 2, 3, 4]), "[1, 2, 3, 4]"),
            (TwoLinkedList([1, 2]), "[1, 2]"),
            (TwoLinkedList([1]), "[1]"),
            (TwoLinkedList([]), "[]"),
        ]
    )
    def test_simple_case(self, two_linked_list: TwoLinkedList, expected: str) -> None:
        assert str(two_linked_list) == expected, f"Ошибка при аргументе: {expected}"


# pytest tests/test_two_linked_list.py


class TestRepr:
    # pytest tests/test_two_linked_list.py::TestRepr
    @pytest.mark.parametrize(
        "two_linked_list, expected",
        [
            (TwoLinkedList([1, 2]), "TwoLinkedList([1, 2])"),
            (TwoLinkedList([1]), "TwoLinkedList([1])"),
            (TwoLinkedList([]), "TwoLinkedList([])"),
        ]
    )
    def test_simple_case(self, two_linked_list: TwoLinkedList, expected: str) -> None:
        assert repr(two_linked_list) == expected, f"Ошибка при: {expected}"


class TestLen:
    # pytest tests/test_two_linked_list.py::TestLen
    @pytest.mark.parametrize(
        "two_linked_list, expected",
        [
            (TwoLinkedList([1, 2, 3]), 3),
            (TwoLinkedList([1, "Hello", [1, 2, 3], True, (1, 2), {"Test": 1}]), 6),
            (TwoLinkedList([]), 0)
        ]
    )
    def test_simple_case(self, two_linked_list: TwoLinkedList, expected: str) -> None:
        assert len(two_linked_list) == expected, f"Ошибка при: {expected}"


class TestAdd:
    # pytest tests/test_two_linked_list.py::TestAdd
    @pytest.mark.parametrize(
        "first_tll, second_tll, expected_tll",
        [
            (TwoLinkedList([1, 2, 3]), TwoLinkedList([4, 5, 6]), TwoLinkedList([1, 2, 3, 4, 5, 6])),
            (TwoLinkedList([1]), TwoLinkedList([4]), TwoLinkedList([1, 4])),
            (TwoLinkedList([1]), TwoLinkedList([]), TwoLinkedList([1])),
            (TwoLinkedList([]), TwoLinkedList([4]), TwoLinkedList([4])),
            (TwoLinkedList([]), TwoLinkedList([]), TwoLinkedList([])),
            (TwoLinkedList([1, 2.0, "Hello"]), TwoLinkedList([[1, 2], (3, 4), {"Test": 1}]),
             TwoLinkedList([1, 2.0, "Hello", [1, 2], (3, 4), {"Test": 1}])),
        ]
    )
    def test_simple_case(self, first_tll: TwoLinkedList, second_tll: TwoLinkedList,
                         expected_tll: TwoLinkedList) -> None:
        assert first_tll + second_tll == expected_tll, f"Ошибка при: {expected_tll}"


class TestContains:
    # pytest tests/test_two_linked_list.py::TestContains
    @pytest.mark.parametrize(
        "two_linked_list, needed_element",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 3),
            (TwoLinkedList([1, 2, 3, 4, 5]), 1),
            (TwoLinkedList([1, 2, 3, 4, 5]), 5),
            (TwoLinkedList([1, 2, 3, 4, 5]), 5.0),
            (TwoLinkedList([1, 2, 3, "Hello", 5]), "Hello"),
            (TwoLinkedList([1]), 1)
        ]
    )
    def test_simple_case_with_contain_element(self, two_linked_list: TwoLinkedList, needed_element: Any) -> None:
        assert needed_element in two_linked_list, f"Ошибка при: {needed_element}"

    @pytest.mark.parametrize(
        "two_linked_list, needed_element",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 6),
            (TwoLinkedList([1, 2, 3, "Hello", 5]), "Hello!"),
            (TwoLinkedList([1]), 2)
        ]
    )
    def test_simple_case_with_not_contain_element(self, two_linked_list: TwoLinkedList, needed_element: Any) -> None:
        assert needed_element not in two_linked_list, f"Ошибка при: {needed_element}"


class TestBool:
    # pytest tests/test_two_linked_list.py::TestBool
    @pytest.mark.parametrize(
        "base_list, two_linked_list",
        [
            (base_list := [1, 2, 3, 4, 5], TwoLinkedList(base_list)),
            (base_list := [1, 2], TwoLinkedList(base_list)),
            (base_list := [1], TwoLinkedList(base_list)),
            (base_list := ["Hello", 2.0], TwoLinkedList(base_list))
        ]
    )
    def test_with_true(self, base_list: list, two_linked_list: TwoLinkedList) -> None:
        assert bool(two_linked_list), f"Ошибка при аргументе: {base_list}"

    @pytest.mark.parametrize(
        "base_list, two_linked_list",
        [
            (base_list := [], TwoLinkedList(base_list))
        ]
    )
    def test_with_false(self, base_list: list, two_linked_list: TwoLinkedList) -> None:
        assert not bool(two_linked_list), f"Ошибка при аргументе: {base_list}"


class TestGetItem:
    # pytest tests/test_two_linked_list.py::TestGetItem
    @pytest.mark.parametrize(
        "two_linked_list, index, expected",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 3, 4),
            (TwoLinkedList([1, 2, 3, 4, 5]), 0, 1),
            (TwoLinkedList([1, 2, 3, 4, 5]), 4, 5),
            (TwoLinkedList([1, "Hello", 3.0, [4], (5,)]), 3, [4]),
        ]
    )
    def test_simple_args(self, two_linked_list: TwoLinkedList, index: int, expected: Any) -> None:
        assert two_linked_list[index] == expected, \
            f"Ошибка при индексе - {index}, ожидалось - {expected}, вернулось - {two_linked_list[index]}"

    @pytest.mark.parametrize(
        "two_linked_list, index, expected",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 10, IndexError),
            (TwoLinkedList([1, 2, 3, 4, 5]), 5, IndexError),
            (TwoLinkedList([1, 2, 3, 4, 5]), -1, ValueError),
            (TwoLinkedList([1, 2, 3, 4, 5]), 2.0, TypeError)
        ]
    )
    def test_error_case(self, two_linked_list: TwoLinkedList, index: int, expected: E) -> None:
        with pytest.raises(expected):
            two_linked_list[index]


class TestSetItem:
    # pytest tests/test_two_linked_list.py::TestSetItem
    @pytest.mark.parametrize(
        "two_linked_list, index, new_value",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 3, 10),
            (TwoLinkedList([1, 2, 3, 4, 5]), 0, 10),
            (TwoLinkedList([1, 2, 3, 4, 5]), 4, 10),
            (TwoLinkedList([1, "Hello", [2.0, 3], (5, 5, 1), True]), 3, {"Test": "Test"})
        ]
    )
    def test_simple_case(self, two_linked_list: TwoLinkedList, index: int, new_value: Any) -> None:
        two_linked_list[index] = new_value
        assert two_linked_list[index] == new_value, f"Ошибка при index={index}"

    @pytest.mark.parametrize(
        "two_linked_list, index, new_value, error",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 10, 10, IndexError),
            (TwoLinkedList([1, 2, 3, 4, 5]), 5, 10, IndexError),
            (TwoLinkedList([1, 2, 3, 4, 5]), -1, 10, ValueError),
            (TwoLinkedList([1, 2, 3, 4, 5]), 2.0, 10, TypeError)
        ]
    )
    def test_error_case(self, two_linked_list: TwoLinkedList, index: int, new_value: Any, error: E) -> None:
        with pytest.raises(error):
            two_linked_list[index] = new_value


class TestDelItem:
    # pytest tests/test_two_linked_list.py::TestDelItem
    @pytest.mark.parametrize(
        "two_linked_list, remove_index, expected",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 3, TwoLinkedList([1, 2, 3, 5])),
            (TwoLinkedList([1, 2, 3, 4, 5]), 0, TwoLinkedList([2, 3, 4, 5])),
            (TwoLinkedList([1, 2, 3, 4, 5]), 4, TwoLinkedList([1, 2, 3, 4])),
            (TwoLinkedList([1, 2.0]), 0, TwoLinkedList([2.0])),
            (TwoLinkedList([1, 2.0]), 1, TwoLinkedList([1])),
            (TwoLinkedList([1]), 0, TwoLinkedList([])),
        ]
    )
    def test_simple_case(self, two_linked_list: TwoLinkedList, remove_index: int, expected: TwoLinkedList) -> None:
        del two_linked_list[remove_index]
        assert two_linked_list == expected, f"Ошибка при: {remove_index}"

    @pytest.mark.parametrize(
        "two_linked_list, remove_index, expected_error",
        [
            (TwoLinkedList([1, 2, 3, 4, 5]), 2.0, TypeError),
            (TwoLinkedList([1, 2, 3, 4, 5]), -1, ValueError),
            (TwoLinkedList([1, 2, 3, 4, 5]), 5, IndexError),
            (TwoLinkedList([]), 1, IndexError)
        ]
    )
    def test_error_case(self, two_linked_list: TwoLinkedList, remove_index: int, expected_error: E) -> None:
        with pytest.raises(expected_error):
            del two_linked_list[remove_index]


class TestCopy:
    # pytest tests/test_two_linked_list.py::TestCopy
    @pytest.mark.parametrize(
        "two_linked_list",
        [
            (TwoLinkedList([1, 2, 3, 4, 5])),
            (TwoLinkedList([1])),
            (TwoLinkedList([])),
            (TwoLinkedList([1, 2.0, "Test", [1, 2, 3, 4, 5], True, (1, 2), {"Test": "Test"}]))
        ]
    )
    def test_simple_case(self, two_linked_list: TwoLinkedList) -> None:
        assert two_linked_list == copy.copy(two_linked_list), f"Ошибка при: {two_linked_list}"



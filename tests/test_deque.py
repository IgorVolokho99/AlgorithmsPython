"""Модуль, который содержит тесты для двусторонней очереди."""
import copy
from typing import Any, TypeVar

import pytest

from dequeue.dequeue import Deque

E = TypeVar("E", bound=Exception)


class TestIter:
    # pytest tests/test_deque.py::TestIter
    @pytest.mark.parametrize(
        "base_list, testing_deque",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list)),
            (base_list := [1, 2], Deque(base_list)),
            (base_list := [1], Deque(base_list)),
            (base_list := [], Deque(base_list)),
            (base_list := [1, 2.0, "Hello", [1, 2, 3], {"test": "test_1"}, (1, 2, 3), True], Deque(base_list)),
        ]
    )
    def test_simple_case(self, base_list: list, testing_deque: Deque) -> None:
        assert list(testing_deque) == base_list, f"Ошибка при: {testing_deque}"


class TestAppend:
    # pytest tests/test_deque.py::TestAppend
    @pytest.mark.parametrize(
        "base_list, testing_deque, append_element",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 6),
            (base_list := [1, 2], Deque(base_list), 3),
            (base_list := [1], Deque(base_list), 2),
            (base_list := [], Deque(base_list), 1),
            (base_list := [1, 2.0, "Hello", [1, 2, 3], {"test": "test_1"}, (1, 2, 3), True], Deque(base_list), None),
        ]
    )
    def test_simple_case(self, base_list: list, testing_deque: Deque, append_element: Any):
        testing_deque.append(append_element)
        base_list.append(append_element)
        assert list(testing_deque) == base_list, f"Ошибка при: {append_element}"


class TestAppendLeft:
    # pytest tests/test_deque.py::TestAppendLeft
    @pytest.mark.parametrize(
        "base_list, testing_deque, append_element",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 6),
            (base_list := [1, 2], Deque(base_list), 3),
            (base_list := [1], Deque(base_list), 2),
            (base_list := [], Deque(base_list), 1),
            (base_list := [1, 2.0, "Hello", [1, 2, 3], {"test": "test_1"}, (1, 2, 3), True], Deque(base_list), None),
        ]
    )
    def test_simple_case(self, base_list: list, testing_deque: Deque, append_element: Any) -> None:
        testing_deque.append_left(append_element)
        base_list = [append_element] + base_list
        assert list(testing_deque) == base_list, f"Ошибка при: {append_element}"


class TestPop:
    # pytest tests/test_deque.py::TestPop
    @pytest.mark.parametrize(
        "base_list, testing_deque",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list)),
            (base_list := [1, 2], Deque(base_list)),
            (base_list := [1], Deque(base_list)),
        ]
    )
    def test_simple_case(self, base_list: list, testing_deque: Deque) -> None:
        assert base_list.pop() == testing_deque.pop(), f"Ошибка при: {base_list}"
        assert base_list == list(testing_deque), f"Ошибка при: {base_list}"

    def test_negative_case(self) -> None:
        testing_deque = Deque([])
        with pytest.raises(IndexError):
            testing_deque.pop()


class TestPopLeft:
    # pytest tests/test_deque.py::TestPopLeft
    @pytest.mark.parametrize(
        "base_list, testing_deque",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list)),
            (base_list := [1, 2], Deque(base_list)),
            (base_list := [1], Deque(base_list)),
        ]
    )
    def test_simple_case(self, base_list: list, testing_deque: Deque) -> None:
        assert base_list.pop(0) == testing_deque.pop_left(), f"Ошибка при: {base_list}"
        assert base_list == list(testing_deque), f"Ошибка при: {base_list}"

    def test_negative_case(self) -> None:
        testing_deque = Deque([])
        with pytest.raises(IndexError):
            testing_deque.pop()


class TestCopy:
    # pytest tests/test_deque.py::TestCopy
    @pytest.mark.parametrize(
        "testing_deque",
        [
            Deque([1, 2, 3, 4, 5]),
            Deque([1, 2]),
            Deque([1]),
            Deque([]),
            Deque([1, 2.0, "Helo", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {"test": "test"}, True, None])
        ]
    )
    def test_simple_case(self, testing_deque: Deque) -> None:
        copy_deque = copy.copy(testing_deque)
        assert list(testing_deque) == list(copy_deque), f"Ошибка при: {testing_deque}"


class TestClear:
    # pytest tests/test_deque.py::TestClear
    @pytest.mark.parametrize(
        "testing_deque",
        [
            Deque([1, 2, 3, 4, 5]),
            Deque([1, 2]),
            Deque([1]),
            Deque([]),
            Deque([1, 2.0, "Helo", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {"test": "test"}, True, None]),
        ]
    )
    def test_simple_case(self, testing_deque: Deque) -> None:
        print(testing_deque)
        testing_deque.clear()
        assert list(testing_deque) == [], f"Ошибка при: {list(testing_deque)}"


class TestExtend:
    # pytest tests/test_deque.py::TestExtend
    @pytest.mark.parametrize(
        "base_list, extend_list",
        [
            ([1, 2, 3], [4, 5]),
            ([1], [4]),
            ([1], []),
            ([], [1]),
        ]
    )
    def test_extend_deque(self, base_list: list, extend_list: list) -> None:
        testing_deque = Deque(base_list)
        extend_deque = Deque(extend_list)
        testing_deque.extend(extend_deque)
        assert list(testing_deque) == base_list + extend_list, f"Ошибка при: {base_list} и {extend_list}"

    @pytest.mark.parametrize(
        "base_list, extend_object",
        [
            ([1, 2, 3], [4, 5]),
            ([1], (1, 2, 3)),
            ([1], {1, 2, 3}),
        ]
    )
    def test_extend_iterable_object(self, base_list: list, extend_object: Any) -> None:
        testing_deque = Deque(base_list)
        testing_deque.extend(extend_object)
        assert list(testing_deque) == base_list + list(extend_object), f"Ошибка при: {base_list} и {extend_object}"

    @pytest.mark.parametrize(
        "base_list, extend_object",
        [
            ([1, 2, 3], 1),
            ([1], True),
            ([1], 2.0),
            ([], None),
        ]
    )
    def test_negative_object(self, base_list: list, extend_object: Any) -> None:
        testing_deque = Deque(base_list)
        with pytest.raises(TypeError):
            testing_deque.extend(extend_object)


class TestExtendLeft:
    # pytest tests/test_deque.py::TestExtendLeft
    @pytest.mark.parametrize(
        "base_list, extend_list",
        [
            ([1, 2, 3], [4, 5]),
            ([1], [4]),
            ([1], []),
            ([], [1]),
        ]
    )
    def test_extend_deque(self, base_list: list, extend_list: list) -> None:
        testing_deque = Deque(base_list)
        extend_deque = Deque(extend_list)
        testing_deque.extend_left(extend_deque)
        assert list(testing_deque) == extend_list + base_list, f"Ошибка при: {base_list} и {extend_list}"

    @pytest.mark.parametrize(
        "base_list, extend_object",
        [
            ([1, 2, 3], [4, 5]),
            ([1], (1, 2, 3)),
            ([1], {1, 2, 3}),
        ]
    )
    def test_extend_iterable_object(self, base_list: list, extend_object: Any) -> None:
        testing_deque = Deque(base_list)
        testing_deque.extend_left(extend_object)
        assert list(testing_deque) == list(extend_object) + base_list, f"Ошибка при: {base_list} и {extend_object}"

    @pytest.mark.parametrize(
        "base_list, extend_object",
        [
            ([1, 2, 3], 1),
            ([1], True),
            ([1], 2.0),
            ([], None),
        ]
    )
    def test_negative_object(self, base_list: list, extend_object: Any) -> None:
        testing_deque = Deque(base_list)
        with pytest.raises(TypeError):
            testing_deque.extend_left(extend_object)


class TestIndex:
    # pytest tests/test_deque.py::TestIndex

    @pytest.mark.parametrize(
        "base_list, testing_deque, needed_pos, needed_value",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 2, 3),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 0, 1),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 4, 5),
            (base_list := [1], Deque(base_list), 0, 1),
        ]
    )
    def test_simple_case(self, base_list: list, testing_deque: Deque, needed_pos: int, needed_value: Any) -> None:
        assert testing_deque.index(needed_value) == needed_pos, f"Ошибка при: value = {needed_value}"

    @pytest.mark.parametrize(
        "base_list, testing_deque, needed_pos, needed_value, start, end",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 2, 3, 1, 4),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 1, 2, 1, 4),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 3, 4, 1, 4)
        ]
    )
    def test_with_start_end(self, base_list: list, testing_deque: Deque, needed_pos: int, needed_value: Any, start: int,
                            end: int) -> None:
        assert testing_deque.index(needed_value, start=start,
                                   end=end) == needed_pos, f"Ошибка при: value = {needed_value}"

    @pytest.mark.parametrize(
        "base_list, testing_deque, needed_value",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10)
        ]
    )
    def test_negative_case_not_in_list(self, base_list: list, testing_deque: Deque, needed_value: Any) -> None:
        with pytest.raises(ValueError):
            testing_deque.index(needed_value)

    @pytest.mark.parametrize(
        "base_list, testing_deque, needed_value, start, end, expected_error",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10, 1.0, 2.5, TypeError),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10, 1, 2.5, TypeError),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10, [1, 2], 10, TypeError),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10, -10, -10, ValueError),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10, -5, 2, ValueError),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10, 2, -10, ValueError),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10, 10, 15, IndexError),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10, 1, 15, IndexError),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 10, 15, 1, IndexError)
        ]
    )
    def test_negative_case_invalid_start_stop(self, base_list: list, testing_deque: Deque, needed_value: Any,
                                              start: Any, end: Any, expected_error: E) -> None:
        with pytest.raises(expected_error):
            testing_deque.index(needed_value, start=start, end=end)


class TestCount:
    # pytest tests/test_deque.py::TestCount
    @pytest.mark.parametrize(
        "testing_deque, needed_value, expected",
        [
            (Deque([1, 2, 3, 4, 5]), 3, 1),
            (Deque([1, 2, 3, 4, 5]), 1, 1),
            (Deque([1, 2, 3, 4, 5]), 5, 1),
            (Deque([1, 2, 3, 1]), 1, 2),
            (Deque([1, 1]), 1, 2),
            (Deque([1]), 1, 1),
            (Deque([]), 1, 0),
            (Deque([1, 2.0, "Hello", [1, 2, 3]]), "By", 0)
        ]
    )
    def test_simple_case(self, testing_deque: Deque, needed_value: Any, expected: int) -> None:
        assert testing_deque.count(needed_value) == expected, f"Ошибка при: {needed_value}"


class TestRemove:
    # pytest tests/test_deque.py::TestRemove
    @pytest.mark.parametrize(
        "base_list, testing_deque, remove_element",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 3),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 1),
            (base_list := [1, 2, 3, 4, 5], Deque(base_list), 5),
            (base_list := [1], Deque(base_list), 1)
        ]
    )
    def test_simple_case(self, base_list: list, testing_deque: Deque, remove_element: Any) -> None:
        testing_deque.remove(remove_element)
        base_list.remove(remove_element)
        assert list(testing_deque) == base_list, f"Ошибка при: {base_list} и {remove_element}"

    def test_negative_case(self) -> None:
        testing_deque = Deque([1, 2, 3, 4, 5])
        with pytest.raises(ValueError):
            testing_deque.remove(10)


class TestReverse:
    # pytest tests/test_deque.py::TestReverse
    @pytest.mark.parametrize(
        "base_list, testing_deque",
        [
            (base_list := [1, 2, 3, 4, 5], Deque(base_list)),
            (base_list := [1, 2], Deque(base_list)),
            (base_list := [1], Deque(base_list)),
            (base_list := [], Deque(base_list)),
            (base_list := [1, 2.0, "3.5", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {"test": "test"}, True], Deque(base_list))
        ]
    )
    def test_simple_case(self, base_list: list, testing_deque: Deque) -> None:
        testing_deque.reverse()
        assert list(testing_deque) == base_list[::-1], f"Ошибка при аргументе: {base_list}"

# pytest tests/test_deque.py

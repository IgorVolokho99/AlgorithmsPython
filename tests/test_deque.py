"""Модуль, который содержит тесты для двусторонней очереди."""
import copy
from typing import Any

import pytest

from dequeue.dequeue import Deque


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




# pytest tests/test_deque.py

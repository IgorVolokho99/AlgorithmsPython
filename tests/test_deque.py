"""Модуль, который содержит тесты для двусторонней очереди."""
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

# pytest tests/test_deque.py

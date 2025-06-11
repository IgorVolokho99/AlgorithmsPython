"""Модуль, который содержит тесты для двусторонней очереди."""

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

# pytest tests/test_deque.py

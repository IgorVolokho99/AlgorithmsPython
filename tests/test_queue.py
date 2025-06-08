"""Модуль, который содержит тесты для структуры queue."""
from typing import Any

import pytest

from queue.queue import Queue


class TestGetSize:
    # pytest tests/test_queue.py::TestGetSize
    @pytest.mark.parametrize(
        "base_list, expected_size",
        [
            ([1, 2, 3], 3),
            ([1, 2], 2),
            ([1], 1),
            ([], 0),
            ([1, 2.0, "Hello", [1, 2, 3], (1, 2, 3), True, {"test": 1}], 7)
        ]
    )
    def test_simple_case(self, base_list: list, expected_size: int) -> None:
        testing_queue = Queue()
        for value in base_list:
            testing_queue.enqueue(value)
        assert testing_queue.get_size() == expected_size, f"Ошибка при длине: {expected_size}"


class TestEnqueueDequeue:
    # pytest tests/test_queue.py::TestEnqueueDequeue
    @pytest.mark.parametrize(
        "base_list, expected_size",
        [
            ([1, 2, 3], 3),
            ([1, 2], 2),
            ([1], 1),
            ([], 0),
            ([1, 2.0, "Hello", [1, 2, 3], (1, 2, 3), True, {"test": 1}], 7)
        ]
    )
    def test_simple_case(self, base_list: list, expected_size: int) -> None:
        testing_queue = Queue()
        for value in base_list:
            testing_queue.enqueue(value)

        for value in base_list:
            assert testing_queue.dequeue() == value, f"Ошибка при аргументе: {value}"

    def test_error_case(self) -> None:
        testing_queue = Queue()
        with pytest.raises(IndexError):
            testing_queue.dequeue()


class TestPeek:
    # pytest tests/test_queue.py::TestPeek
    @pytest.mark.parametrize(
        "base_list, first_value",
        [
            ([1, 2, 3], 1),
            ([1.0, 2], 1.0),
            ([True], True),
            (["1", 2.0, "Hello", True, [1, 2, 3], (1, 2), {"Test": "Hello"}], "1")
        ]
    )
    def test_simple_case(self, base_list: list, first_value: Any) -> None:
        testing_queue = Queue()
        for value in base_list:
            testing_queue.enqueue(value)
        testing_queue.enqueue(first_value)
        assert testing_queue.peek() == first_value, f"Последнее значение: {first_value}"

    def test_peek_from_empty_list(self) -> None:
        testing_queue = Queue()
        with pytest.raises(IndexError):
            testing_queue.peek()


class TestIsEmpty:
    # pytest tests/test_queue.py::TestIsEmpty --durations=0 --verbose
    def test_empty_queue(self) -> None:
        testing_queue = Queue()
        assert testing_queue.is_empty()

        testing_queue.enqueue(1)
        testing_queue.dequeue()
        assert testing_queue.is_empty()

        testing_queue.enqueue(1)
        testing_queue.enqueue(2)
        testing_queue.enqueue(3)
        testing_queue.dequeue()
        testing_queue.dequeue()
        testing_queue.dequeue()

        assert testing_queue.is_empty()

    def test_not_empty_queue(self) -> None:
        testing_queue = Queue()

        testing_queue.enqueue(1)
        assert not testing_queue.is_empty()

        testing_queue.enqueue(1)
        testing_queue.enqueue(2)
        testing_queue.enqueue(3)
        testing_queue.dequeue()
        assert not testing_queue.is_empty()


class TestLen:
    # pytest tests/test_queue.py::TestLen --durations=0 --verbose
    @pytest.mark.parametrize(
        "base_list",
        [
            ([1, 2, 3]),
            ([1, 2]),
            ([1]),
            ([]),
            ([1, 2.0, "3", "hello World", True])
        ]
    )
    def test_queue_with_values(self, base_list: list) -> None:
        testing_queue = Queue()
        for value in base_list:
            testing_queue.enqueue(value)

        assert len(testing_queue) == len(base_list), f"Ошибка при входном аргументе: {base_list}"

    def test_empty_queue(self) -> None:
        testing_queue = Queue()
        assert len(testing_queue) == 0, f"Ошибка при пустой очереди."


class TestBool:
    # pytest tests/test_queue.py::TestBool --durations=0 --verbose
    def test_empty_queue(self) -> None:
        testing_queue = Queue()
        assert not testing_queue

        testing_queue.enqueue(1)
        testing_queue.dequeue()
        assert not testing_queue

        testing_queue.enqueue(1)
        testing_queue.enqueue(2)
        testing_queue.enqueue(3)
        testing_queue.dequeue()
        testing_queue.dequeue()
        testing_queue.dequeue()

        assert not testing_queue

    def test_not_empty_queue(self) -> None:
        testing_queue = Queue()

        testing_queue.enqueue(1)
        assert testing_queue

        testing_queue.enqueue(1)
        testing_queue.enqueue(2)
        testing_queue.enqueue(3)
        testing_queue.dequeue()
        assert testing_queue


class TestStr:
    # pytest tests/test_queue.py::TestStr --durations=0 --verbose
    @pytest.mark.parametrize(
        "base_list",
        [
            ([1, 2, 3, 4, 5]),
            ([1, 2]),
            ([1]),
            ([])
        ]
    )
    def test_simple_case(self, base_list: list) -> None:
        testing_queue = Queue()
        for value in base_list:
            testing_queue.enqueue(value)

        assert str(testing_queue) == f"Node({base_list})", f"Ошибка при аргументе: {base_list}"

# pytest tests/test_queue.py --durations=0 --verbose

"""Модуль, который содержит тесты для структуры queue."""
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

# pytest tests/test_queue.py --durations=0 --verbose

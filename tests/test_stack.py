"""Модуль, который содержит тесты для структуры stack."""
from typing import Any, TypeVar

import pytest

from stack.stack import Stack

E = TypeVar("E", bound=IndexError)


class TestPush:
    # pytest tests/test_stack.py::TestPush
    @pytest.mark.parametrize(
        "testing_stack, value",
        [
            (Stack(), 1),
            (Stack(), 0),
            (Stack(), -10),
            (Stack(), "-10"),
            (Stack(), ["Hello World!", 1, 2.0, True])
        ]
    )
    def test_simple_case(self, testing_stack: Stack, value: Any) -> None:
        testing_stack.push(value)
        assert testing_stack._top.value == value, f"Ошибка при: {value}"


class TestPop:
    # pytest tests/test_stack.py::TestPop
    @pytest.mark.parametrize(
        "testing_stack, value",
        [
            (Stack(), 1),
            (Stack(), 0),
            (Stack(), -10),
            (Stack(), "-10"),
            (Stack(), ["Hello World!", 1, 2.0, True])
        ]
    )
    def test_simple_case(self, testing_stack: Stack, value: Any) -> None:
        testing_stack.push(value)
        assert testing_stack.pop() == value, f"Ошибка при: {value}"

    @pytest.mark.parametrize(
        "testing_stack, exception",
        [
            (Stack(), IndexError)
        ]
    )
    def test_pop_from_empty_list(self, testing_stack: Stack, exception: E) -> None:
        with pytest.raises(exception):
            testing_stack.pop()


class TestGetSize:
    # pytest tests/test_stack.py::TestGetSize
    @pytest.mark.parametrize(
        "testing_stack, values",
        [
            (Stack(), [1, 2, 3, 4, 5]),
            (Stack(), []),
            (Stack(), [10, 3, "Hello World"]),
        ]
    )
    def test_simple_case(self, testing_stack: Stack, values: list) -> None:
        for value in values:
            testing_stack.push(value)
        assert testing_stack.get_size() == len(values), f"Ошибка при: {values}"

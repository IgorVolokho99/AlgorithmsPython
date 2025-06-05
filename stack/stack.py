"""Пакет, содержащий реализацию структуры данных - стек."""
from typing import Any

from stack.node import Node


class Stack:
    """Класс, содержащий реализацию структуры данных - стек."""

    def __init__(self) -> None:
        """Инициализирует экземпляр класс Node.

        Создается два поля: top и size. top хранит указатель на вершину стека. size хранит количество элементов в стеке.
        """
        self._top = None
        self._size = 0

    def push(self, value: Any) -> None:
        """Метод, который добавляет элемент на вершину стека.

        Оценка сложности по времени: O(1);
        Оценка сложности по памяти: O(1);

        Args:
            value(Any): Значение, которое будет добавлено на вершину.

        """
        new_node = Node(value)
        new_node.next_node = self._top
        self._top = new_node
        self._size += 1

    def pop(self) -> Any:
        """Метод, который возвращает элемент с вершины стека.

        Оценка сложности по времени: O(1);
        Оценка сложности по памяти: O(1);

        Returns:
            Any: Значение, которое лежит на вершине стека.

        """
        if self._top is None:
            raise IndexError("Can not pop from empty stack.")
        value = self._top.value
        self._top = self._top.next_node
        self._size -= 1
        return value

    def get_size(self) -> int:
        """Возвращает количество элементов в стеке.

        Оценка сложности по времени: O(1);
        Оценка сложности по памяти: O(1);

        Returns:
            int: Количество элементов стека.

        """
        return self._size

"""Модуль, который содержит реализацию структуры данных Queue."""

from typing import Any

from queue.node import Node


class Queue:
    """Класс, реализующий структуру очереди с дисциплиной доступа FIFO."""

    def __init__(self) -> None:
        """Инициализирует пустую очередь с вершиной и хвостом равными None и длиной 0."""
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value: Any) -> None:
        """Добавляет значение в конец очереди.

        Args:
            value(Any): Объект любого типа, который будет добавлен в конец очереди.

        """
        new_node = Node(value)

        if self._tail is None:
            self._tail = self._head = new_node
        else:
            self._tail.next_node = new_node
            self._tail = new_node

        self._size += 1

    def dequeue(self) -> Any:
        """Удаляет и возвращает значение из начала очереди.

        Returns:
            Any: Значение узла, который находится в начале очереди.

        """
        if self._head is None:
            raise IndexError("Can not dequeue from empty queue.")

        value = self._head.value

        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next_node

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

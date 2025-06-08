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

        Оценка сложности по времени: O(1);
        Оценка сложности по памяти: O(1);

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

        Оценка сложности по времени: O(1);
        Оценка сложности по памяти: O(1);

        Returns:
            Any: Значение узла, который находится в начале очереди.

        Raises:
            IndexError: Бросается, если метод вызывается на пустой очереди.

        """
        if self._head is None:
            raise IndexError("Can not dequeue from empty queue.")

        value = self._head.value

        self._head = self._head.next_node
        if self._head is None:
            self._tail = None

        self._size -= 1

        return value

    def get_size(self) -> int:
        """Возвращает количество элементов в очереди.

        Оценка сложности по времени: O(1);
        Оценка сложности по памяти: O(1);

        Returns:
            int: Количество элементов стека.

        """
        return self._size

    def peek(self) -> Any:
        """Возвращает значение узла из начала очереди.

        Returns:
            Any: Значение, которое хранится в начале очереди.

        Raises:
            IndexError: Происходит, если запрашивается элемент из пустой очереди.

        """
        if self._head is None:
            raise IndexError("Can not peep from empty queue.")

        return self._head.value

    def is_empty(self) -> bool:
        """Возвращает True, если очередь пустая и False в противном случае.

        Returns:
            bool: Булевый литерал, который является флагом пустоты очереди.

        """
        return True if self.get_size() == 0 else False

    def __len__(self) -> int:
        """Магический метод, который возвращает количество элементов в очереди.

        Returns:
            int: Количество элементов в очереди.

        """
        return self.get_size()

    def __bool__(self) -> bool:
        """Позволяет использовать экземпляры класса в bool выражениях.

        Returns:
            bool: True, если экземпляр не пуст и False в противном случае.

        """
        return not self.is_empty()

    def __str__(self) -> str:
        """Магический метод, возвращаются строковую интерпертацию экземпляра класса.

        Returns:
            str: Строка вида Node([1, 2, 3]).

        """
        base_list = []
        current_node = self._head
        while current_node:
            base_list.append(current_node.value)
            current_node = current_node.next_node

        return f"Node({base_list})"

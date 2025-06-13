"""Модуль, содержащий реализацию двусторонней очереди(Dequeue)."""
from typing import Iterable, Any, Iterator

from dequeue.node import Node


class Deque:
    """Реализация двусторонней очереди."""

    def __init__(self, iterable: Iterable, maxlen: int = None) -> None:
        """Инициализирует пустую двустороннюю очередь значениями итерируемого объекта и None для атрибута max_len.

        Args:
            iterable(Iterable): Итерируемая коллекция, объекты которой будут сохранены в очередь;
            maxlen(int): Число, которое будет задавать ограничение на максимальное количество объектов в очереди.

        """
        self._head = None
        self._tail = None
        self._size = 0
        self._max_len = maxlen

        for value in iterable:
            if self._head is None:
                self._head = self._tail = Node(value)
            else:
                new_node = Node(value)
                new_node.prev = self._tail
                self._tail.next = new_node
                self._tail = new_node

            self._size += 1

    def append(self, value: Any) -> None:
        """Добавляет элемент в конец очереди.

        Args:
            value(Any): Значение, которое будет сохранено в конечный узел.

        """
        if self._tail is None:
            self._head = self._tail = Node(value)
        else:
            new_node = Node(value)
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def __iter__(self) -> Iterator[Any]:
        """Позволяет итерироваться по элементам дека от головы к хвосту.

        Yields:
            Any: Значения узлов, начиная от головы и до хвоста.

        """
        current_node = self._head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def append_left(self, value: Any) -> None:
        """Добавляет элемент в начало очереди.

        Args:
            value(Any): Значение, которое будет сохранено в конечный узел.

        """
        if self._head is None:
            self._head = self._tail = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

    # def pop(self) -> Any:
    #     pass
    #
    # def pop_left(self) -> Any:
    #     pass
    #
    # def copy(self) -> "Dequeue":
    #     pass
    #
    # def clear(self) -> None:
    #     pass
    #
    # def extend(self, iterable: Iterable) -> None:
    #     pass
    #
    # def extend_left(self, iterable: Iterable) -> None:
    #     pass
    #
    # def index(self, value: Any) -> int:
    #     pass  # Will check signature of implemantation stadart dequeue from collections
    #
    # def count(self, value: Any) -> int:
    #     pass  # Will check
    #
    # def rotate(self, n: int) -> None:
    #     pass  # Will check
    #
    # def reverse(self) -> None:
    #     pass
    #
    # def remove(self, value: Any) -> None:
    #     pass  # Will check
    #
    # def insert(self, value: Any, pos: index) -> None:
    #     pass  # Will check

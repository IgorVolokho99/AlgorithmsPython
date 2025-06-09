"""Модуль, содержащий реализацию двусторонней очереди(Dequeue)."""
from typing import Iterable

from dequeue.node import Node


class Dequeue:
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

    # def append(self, value: Any) -> None:
    #     pass
    #
    # def append_left(self, value: Any) -> None:
    #     pass
    #
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

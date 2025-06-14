"""Модуль, содержащий реализацию двусторонней очереди(Dequeue)."""
import collections
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
            self._size += 1

    def pop(self) -> Any:
        """Удаляет и возвращает последний элемент двусторонней очереди.

        Returns:
            Any: Значение последнего узла очереди.

        Raises:
            IndexError: Если попытка удалить элемент из пустой очереди.

        """
        if self._head is None:
            raise IndexError("Can not pop from an empty list.")

        if self._head is self._tail:
            value = self._tail.value
            self._head = self._tail = None
            self._size -= 1
            return value

        value = self._tail.value
        self._tail = self._tail.prev
        self._tail.next = None
        self._size -= 1
        return value

    def pop_left(self) -> Any:
        """Удаляет и возвращает первый элемент двусторонней очереди.

        Returns:
            Any: Значение первого узла очереди.

        Raises:
            IndexError: Если попытка удалить элемент из пустой очереди.

        """
        if self._head is None:
            raise IndexError("Can not pop from an empty list.")

        if self._head is self._tail:
            value = self._head.value
            self._head = self._tail = None
            self._size -= 1
            return value

        value = self._head.value
        self._head = self._head.next
        self._head.prev = None
        self._size -= 1
        return value

    def __copy__(self) -> "Deque":
        """Магический метод, создающий поверхностную копию экземпляра класса.

        Возвращает поверхностную копию экземпляра класса. Вызывается функцией copy модуля copy.

        Returns:
            Deque: Поверхностная копия экземпляра класса.

        """
        new_obj = Deque([])

        for value in self:
            new_obj.append(value)

        return new_obj

    def clear(self) -> None:
        """Очищает двустороннюю очередь."""
        self._head = self._tail = None
        self._size = 0

    def extend(self, iterable: Iterable) -> None:
        """Добавляет по очереди все элементы итерируемой коллекции в конец двусторонней очереди.

        Args:
            iterable: Коллекция, элементы которой будут добавлены в очередь.

        Raises:
            TypeError: Если переданный объект не является итерируемым.

        """
        if not isinstance(iterable, collections.abc.Iterable):
            raise TypeError("Argument must be an iterable object")

        for value in iterable:
            self.append(value)

    def extend_left(self, iterable: Iterable) -> None:
        """Добавляет по очереди все элементы итерируемой коллекции в начала двусторонней очереди.

        Args:
            iterable: Коллекция, элементы которой будут добавлены в очередь.

        Raises:
            TypeError: Если переданный объект не является итерируемым.

        """
        if not isinstance(iterable, collections.abc.Iterable):
            raise TypeError("Argument must be an iterable object")

        for value in reversed(list(iterable)):
            self.append_left(value)

    def index(self, needed_value: Any, start: int = None, end: int = None) -> int:
        """Возвращает индекс первого вхождения указанного значения в пределах диапазона.

        Args:
            needed_value (Any): Искомое значение;
            start (int): Индекс, с которого начинается поиск (по умолчанию 0);
            end (int): Индекс, до которого ведётся поиск (по умолчанию — конец очереди).

        Returns:
            int: Индекс первого найденного элемента.

        Raises:
            TypeError: Если start или end не являются целыми числами;
            ValueError: Если значение не найдено;
            IndexError: Если start или end выходят за границы.

        """
        if start is None:
            start = 0
        if end is None:
            end = self._size

        if not isinstance(start, int):
            raise TypeError(f"List index must be integer, not {type(start)}")

        if not isinstance(end, int):
            raise TypeError(f"List index must be integer, not {type(end)}")

        if start < 0 or end < 0:
            raise ValueError("List index must be whole.")

        if start > self._size or end > self._size:
            raise IndexError("List index out of range.")

        for i, current_value in enumerate(list(self)[start:end], start=start):
            if current_value == needed_value:
                return i

        raise ValueError(f"{needed_value} is not in list")

    def count(self, needed_value: Any) -> int:
        """Подсчитывает количество вхождений value в очередь.

        Args:
            needed_value(Any): Искомое значение для подсчета.

        Returns:
            int: Количество вхождение value в очередь.

        """
        counter = 0
        for current_value in self:
            if current_value == needed_value:
                counter += 1
        return counter

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

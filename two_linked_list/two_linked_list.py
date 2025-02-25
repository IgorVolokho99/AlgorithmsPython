from typing import Any

from two_linked_list.node import Node


class TwoLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        """Метод, проверяющий является ли список пуст.

        Returns:
            bool: True, если список пуст и False в противном случае.

        """
        return self.head is None

    def push_back(self, value: Any) -> None:
        """Метод, добавляющий значение в конец списка.

        Создает объект типа Node, который инициализируем значением value и добавляем в конец списка, изменяя
        значение tail.
        Args:
            value: значение, которое будет добавлено в конец списка.

        """
        new_node = Node(value)
        if not self.is_empty():
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = self.tail = new_node

    def pop_back(self):
        pass

    def push_front(self):
        pass

    def pop_front(self):
        pass

    def insert(self):
        pass

    def remove(self):
        pass

    def find(self):
        pass

    def get(self):
        pass

    def set(self):
        pass

    def size(self):
        pass

    def reverse(self):
        pass

    def clear(self):
        pass

    def extend(self):
        pass

    def __copy__(self):
        pass

    def __deepcopy__(self, memodict={}):
        pass

    def __add__(self, other):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __reversed__(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self, item):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __bool__(self):
        pass

"""Модуль, содержащий в себе реализацию односвязного списка."""

from typing import Any

from node import Node


class OneLinkedList:
    """Класс, реализующий односвязный список."""

    def __init__(self, node: Node = None):
        """Конструктор класса OneLinkedList.

        Принимает необязателньый аргумент node, который по умолчанию сохраняется в атрибуты head и tail.
        :param node: Необязательный аргумент.
        """
        self.head = node
        self.tail = node

    def is_empty(self) -> bool:
        """Метод, выполняющий проверку пустоты односвязного списка."""
        return True if self.head is None else False

    def push_back(self, data: Any) -> None:
        """Добавление элемента в односвязный список.

        Метод, принимающий на вход объект любого типа из которого формируется экземпляр класса Node и добавляется
        в односвянзный список. В зависимости от того пуст список или нет объект может быть добавлен в атрибут head.
        :param data: Объект любого типа.
        :return: None
        """
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def pop_back(self):
        """Метод удаляющий последний элемент односвязного списка.

        Метод, который удаляет последний элемент с конца списка. В случае, если список пуст, то генерируется исключение
        IndexError. В случае, если список, состоит из одного элемента, то выполняется алгоритм ручного удаления за O(1).
        В остальных случаях выполняется поиск предпоследнего элемента и удаление следующего за ним за O(n).
        :return: значение удаленного узла.
        """
        if self.head is None:
            raise IndexError("pop from empty one linked list")
        elif self.head == self.tail:
            value = self.head.value
            self.head = self.tail = None
            return value
        else:
            node = self.head
            while node.next != self.tail:
                node = node.next

            value = node.next.value
            self.tail = node
            node.next = None

            return value

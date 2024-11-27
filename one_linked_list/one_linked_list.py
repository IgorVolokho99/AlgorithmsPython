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

    def append(self, data: Any) -> None:
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

"""Модуль, содержащий в себе реализацию односвязного списка."""

from typing import Any

from .node import Node


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

        Args:
            data: Объект любого типа.

        Returns:
            None.

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

        Returns:
            Значение удаленного узла.

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

    def push_front(self, data: Any) -> None:
        """Метод, который добавляет новый узел в начало списка.

        Args:
            data: добавляемое значение.

        Returns:
            None.
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def pop_front(self) -> None:
        """Метод, удаляющий первый узел списка.

        Метод, который удаляет узел из начала односвязного списка.
        Бросает исключение IndexError, если односвязный список пуст.

        Returns:
            None.

        """
        if self.is_empty():
            raise IndexError("List index out of range.")
        self.head = self.head.next

    def insert(self, index: int, data: Any) -> None:
        """Метод, вставляющий значение на позицию index.

        Метод, который принимает data, создает объект Node со значением data и вставляет данный узел в позицию index.
        Вызывается исключение IndexError, если указанного индекса не существуетю

        Args:
            index: позиция, на которую требуется вставить новый узел.
            data: данные, которые будет содержать новый узел.

        Returns:
            None.

        """
        if self.is_empty() and index == 0:
            self.head = Node(data)
            return
        elif self.is_empty() and index > 0:
            raise IndexError("List index out of range")
        elif index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        k = 0
        current_node = self.head
        while k != index - 1:
            current_node = current_node.next
            k += 1
            if current_node is None:
                raise IndexError("List index out of range")

        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data: Any) -> None:
        """Удаляет первый узел со значением data.

        Args:
            data: Значение, которое будет удалено из списка.

        """
        if self.is_empty():
            raise ValueError("list.remove(x): x not in list")
        if self.head.value == data:
            self.pop_front()
            return

        current_node = self.head
        while current_node.next is not None and current_node.next.value != data:
            current_node = current_node.next

        next_node = current_node.next
        if next_node is None:
            raise ValueError("list.remove(x): x not in list")
        elif next_node is self.tail:
            self.tail = current_node
            self.tail.next = None
        else:
            current_node.next = next_node.next

    def find(self, data: Any) -> int:
        """Возвращает индекс первого узла со значением data и -1 в случае отсутствия.

        Args:
            data: Значение, по которому будет выполняться поиск.

        Returns:
            int: Индекс первого элемента со значением data и -1 в случае его отсуствия.

        """

        if self.is_empty():
            return -1
        current_node = self.head
        index = 0
        while current_node.value != data and current_node is not self.tail:
            current_node = current_node.next
            index += 1

        if current_node.value != data:
            return -1

        return index

    def show(self) -> None:
        """Выводит на экран односвязный список.

        Итеративно перебирает узлы односвязного списка и выводит их на экран. Работает за O(n).

        Returns:
            None.

        """
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

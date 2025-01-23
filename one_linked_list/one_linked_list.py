"""Модуль, содержащий в себе реализацию односвязного списка."""

from typing import Any
from copy import deepcopy

from one_linked_list.node import Node


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

    def pop_back(self) -> Any:
        """Метод удаляющий последний элемент односвязного списка.

        Метод, который удаляет последний элемент с конца списка. В случае, если список пуст, то генерируется исключение
        IndexError. В случае, если список, состоит из одного элемента, то выполняется алгоритм ручного удаления за O(1).
        В остальных случаях выполняется поиск предпоследнего элемента и удаление следующего за ним за O(n).

        Returns:
            Any: Значение удаленного узла.

        Raises:
            IndexError: В случае, если список пуст.

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
            self.tail = self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def pop_front(self) -> Any:
        """Метод, удаляющий первый узел списка.

        Метод, который удаляет узел из начала односвязного списка.
        Бросает исключение IndexError, если односвязный список пуст.

        Returns:
            Any: Значение, первого узла.

        Raises:
            IndexError: В случае, если список пуст.

        """
        if self.is_empty():
            raise IndexError("List index out of range.")

        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return value

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

    def get(self, index: int) -> Any:
        """Возвращает значение элемента по указанному индексу.

        Получает целочисленное значение, выступающее индексом списка и возвращает значение узла, которое находится
        под указанным индексом. В случае, если указанного индекса не существует генерируется исключение.
        Args:
            index: Индекс узла значение которого будет возвращено.

        Returns:
            Any: Значение, которое будет возвращено.

        """
        if index < 0:
            raise ValueError("List indexes must be positive integer.")

        current_node = self.head
        i = 0
        while current_node and i < index:
            current_node = current_node.next
            i += 1

        if current_node is None:
            raise IndexError("List index out of range.")

        return current_node.value

    def set(self, index: int, data: Any) -> None:
        """Изменяет значение узла на указанной позиции.

        Принимает целое неотрицательное число(индекс) и некоторое значение, которое будет сохранено в узел по указанной
        позиции. В случае, если индекса не существует генерируется исключение Indexerror.
        Args:
            index: Индекс узла по которому будет происходить обновление значения.
            data: Вставляемое значение.
        """
        if type(index) != int:
            raise TypeError("List indexes must be integer.")
        if index < 0:
            raise ValueError("List indexes must be positive.")

        current_node = self.head
        i = 0
        while current_node and i < index:
            current_node = current_node.next
            i += 1

        if current_node is None:
            raise IndexError("List index out of range.")
        current_node.value = data

    def size(self) -> int:
        """Возвращает количество узлов в списке.

        Returns:
            int: Количество узлов в списке.
        """
        counter = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            counter += 1
        return counter

    def reverse(self) -> None:
        """Метод, который делает reverse односвязного списка.

        Изменяется текущий экземпляр класса, а не возвращается новый.
        """
        self_obj = OneLinkedList()
        current_node = self.head

        while current_node is not None:
            self_obj.push_front(current_node.value)
            current_node = current_node.next

        self.head = self_obj.head
        self.tail = self_obj.tail

    def clear(self) -> None:
        """Очищает экземпляр класса."""
        while self.head is not None:
            self.pop_front()

    def extend(self, other) -> None:
        """Метод, добавляющий все элементы списка other в конец экземпляра класса.

        Raises:
            TypeError: В случае, если other не является экземпляром класса OneLinkedList.
        """
        if not isinstance(other, OneLinkedList):
            raise TypeError("OneLinkedList.extend(x). x must hase type OneLinkedList.")

        for item in other:
            self.push_back(item)

    def __copy__(self):
        """Магический метод, создающий поверхностную копию экземпляра класса.

        Возвращает поверхностную копию экземпляра класса. Вызывается функцией copy модуля copy.
        Returns:
            OneLinkedList: Поверхностная копия экземпляра класса.

        """
        new_list = OneLinkedList()

        for item in self:
            new_list.push_back(item)

        return new_list

    def __deepcopy__(self, memodict={}):
        """Магический метод, создающий глубокую копию экземпляра класса.

        Возвращает глубокую копию экземпляра класса. Вызывается функцией copy модуля copy.
        Returns:
            OneLinkedList: Глубокая копия экземпляра класса.

        """
        if id(self) in memodict:
            return memodict[id(self)]

        new_list = OneLinkedList()
        memodict[id(self)] = new_list

        for item in self:
            new_list.push_back(deepcopy(item, memodict))

        return new_list

    def __add__(self, other):
        """Метод, конкатенирующий два односвязных списка

        Returns:
            OneLinkedList: Односвязных список, в котором сначала идут все значения списка self, а потом все значения
            списка other.

        Raises:
            TypeError: Если объект other не является экземпляром класса OneLinkedList.
        """
        if not isinstance(other, OneLinkedList):
            raise TypeError(f"unsupported operand type(s) for +: 'OneLinkedList' and {type(other)}")

        obj = OneLinkedList()

        for item in self:
            obj.push_back(item)

        for item in other:
            obj.push_back(item)

        return obj

    def __len__(self) -> int:
        """Магический метод, возвращающий к-во элементов односвязного списка.

        Магический метод, который возвращает к-во элементов односвязного списка. Делает совместимым экземпляры данного
        класса с функцией len.
        Returns:
            int: количество элементов односвязного списка.

        """
        return self.size()

    def __str__(self) -> str:
        """Магический метод, возвращающий строковое удобочитаемое представление экземпляра класса.

        Returns:
            str: Строковое удобочитаемое представление экземпляра.

        """
        if self.is_empty():
            return "one_linked_list(size=0)"

        s = 'one_linked_list('
        current_node = self.head
        while current_node is not None:
            if current_node is self.tail:
                s += f"{self.tail.value})"
            else:
                s += f"{current_node.value}->"
            current_node = current_node.next

        return s

    def __eq__(self, other) -> bool:
        """Магический метод, сравнивающий два экземпляра класса.

        Проверяет тип элемента other, если это не объект класса OneLinkedList возвращает False, иначе итеративно прохо-
        дит по каждому узлу self и other сравнивая их, если находит различие узлов возвращает False, иначе возвращает
        True.
        Args:
            other: Объект OneLinkedList.

        Returns:
            bool: True, если объекты одинаковы и False в противном случае.

        """
        if not isinstance(other, OneLinkedList):
            return False
        node_1 = self.head
        node_2 = other.head
        while node_1 is not None:
            if node_1 != node_2 or node_2 is None:
                return False
            node_1 = node_1.next
            node_2 = node_2.next
        if node_2 is not None:
            return False
        return True

    def __iter__(self) -> Any:
        """Магический метод, предназначенный для итерации по списку.

        Генератор, который по очереди возвращает значение каждого узла начиная с head и заканчивая tail.
        Yields:
            Any: Значение узлов списка.

        """
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def __contains__(self, data: Any) -> bool:
        """Магический метод, проверяющий наличие значения data в списке.

        Реализован при помощи метода find.
        Args:
            data: Искомое значение.

        Returns:
            bool: True, если такой элемент присутствует в списке и False в противном случае.

        """
        return True if self.find(data) != -1 else False

    def __getitem__(self, index: int) -> Any:
        """Магический метод, реализующий оператор взятия индекса [].

        Args:
            index: Индекс нужного элемента.

        Returns:
            Any: Значение узла по указанному индексу.

        Raises:
            TypeError: В случае, если получен index не типа данных int.
            IndexError: В случае, если индекс является отрицательным целым числом или лежит вне имеющегося диапазона.

        """
        if not isinstance(index, int):
            raise TypeError("list indices must be integers or slices, not float")
        if index < 0:
            raise IndexError("list indexes must be whole.")

        current_node = self.head
        current_index = 0
        while current_index != index and current_node is not None:
            current_node = current_node.next
            current_index += 1

        if current_index != index or current_node is None:
            raise IndexError("list index out of range.")

        return current_node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """Магический метод, реализующий присваивание по индексу.

        Args:
            index: Индекс, по которому требуется выполнить присваивание.
            value: Значение, которое будет сохранено в узел по указаному индексу.

        Raises:
            TypeError: В случае, если получен index не типа данных int.
            IndexError: В случае, если индекс является отрицательным целым числом или лежит вне имеющегося диапазона.

        """
        if not isinstance(index, int):
            raise TypeError("list indices must be integers or slices, not float")
        if index < 0:
            raise IndexError("list indexes must be whole.")

        current_node = self.head
        current_index = 0
        while current_index != index and current_node is not None:
            current_node = current_node.next
            current_index += 1

        if current_index != index or current_node is None:
            raise IndexError("list index out of range.")

        current_node.value = value

    def __delitem__(self, index: int) -> None:
        """Магический метод, реализующий удаление по индексу.

        Args:
            index: Индекс узла, который требуется удалить.

        Raises:
            TypeError: В случае, если получен index не типа данных int.
            IndexError: В случае, если индекс является отрицательным целым числом или лежит вне имеющегося диапазона.


        """
        if not isinstance(index, int):
            raise TypeError("list indices must be integers or slices, not float")
        if index < 0:
            raise IndexError("list indexes must be whole.")
        if self.is_empty():
            raise IndexError("list index out of range.")
        if index == 0:
            self.pop_front()
            return

        current_node = self.head
        current_index = 0
        while current_index != index - 1 and current_node is not None:
            current_node = current_node.next
            current_index += 1

        if current_index != index - 1 or current_node is None or current_node.next is None:
            raise IndexError("list index out of range.")

        if current_node.next is self.tail:
            self.pop_back()
            return

        current_node.next = current_node.next.next

    def __bool__(self) -> bool:
        """Магический метод булевых операций.

        Метод, который используется для функции bool и использования экземлпяров класса в булевых выражениях. Реализует
        логику Truthy и Falsy значений.
        Returns:
            bool: True, если значение экземпляра является Truthy и False в противном случае.

        """
        return False if self.is_empty() else True

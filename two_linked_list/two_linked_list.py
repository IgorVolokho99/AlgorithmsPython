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
            new_node.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = self.tail = new_node

    def pop_back(self) -> Any:
        """Метод, удаляющий последний элемент списка.

        Происходит проверка, что список пуст и если так, то генерируем исключение IndexError. В случае, если список
        состоит только из одного элемента, то главным узлам head и tail присваиваем None. Иначе просто сдвигаем
        указатель tail на один узел влево. Во всех случаях возвращаем значение удаляемого узла.
        Returns:
            Any: значение удаляемого узла.

        """
        if self.is_empty():
            raise IndexError("Pop from empty list.")
        if self.head is self.tail:
            pop_value = self.head
            self.head = self.tail = None
            return pop_value
        else:
            pop_value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            return pop_value

    def push_front(self, value: Any) -> None:
        """Метод, добавляющий значение в начало списка.

        Создает обьект типа Node, который инициализируется значением value. Если список пуст, то делаем новый узел
        значением head и tail, иначе - обновлям значение head, указывая next и prev связи.
        Args:
            value: значение, которое будет добавлено в начало списка.

        """
        if self.is_empty():
            self.head = self.tail = Node(value)
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = self.head.prev

    def pop_front(self) -> Any:
        """Метод, удаляющий первый элемент списка.

        Происходит проверка, что список пуст и если так, то генерируем исключение IndexError. В случае, если список
        состоит только из одного элемента, то главным узлам head и tail присваиваем None. Иначе просто сдвигаем
        указатель head на один узел вправо. Во всех случаях возвращаем значение удаляемого узла.
        Returns:
            Any: значение удаляемого узла.

        """
        if self.is_empty():
            raise IndexError("Pop from empty list.")
        if self.head is self.tail:
            pop_value = self.head.value
            self.head = self.tail = None
            return pop_value
        else:
            pop_value = self.head.value
            self.head = self.head.next
            self.head.prev = None
            return pop_value

    def insert(self, index: int, value: Any):
        if index >= self.size():
            raise IndexError("List index out of range.")
        if index == 0:
            self.push_front(value)
            return

        current_node = self.head
        current_index = 0
        while current_index != index - 1:
            current_node = current_node.next
            current_index += 1

        if current_node is self.tail:
            self.push_back(value)
            return

        prev_node = current_node
        next_node = current_node.next
        new_node = Node(value)

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = next_node
        new_node.prev = new_node

    def remove(self, value: Any):
        """Метод, удаляющий первый узел со значение value из списка.

        Идем по списку, начиная с head и до узла со значением value(или None). Если дошли до конца списка(None), то
        генерируем исключение ValueError, игаче удаляем узел, который был получен в процессе поиска(с проверкой на
        удаление head или tail).
        Args:
            value: Значение узла, который нужно удалить.

        """
        current_node = self.head

        while current_node and current_node.value != value:
            current_node = current_node.next

        if current_node is None:
            raise ValueError("list.remove(x): x not in list.")

        if current_node is self.head:
            self.pop_front()
        elif current_node is self.tail:
            self.pop_back()
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node

    def find(self):
        pass

    def get(self):
        pass

    def set(self):
        pass

    def size(self) -> int:
        """Метод, возвращающий длину списка.

        Начинаем идти по узлам от head до тех пор, пока не достигнем узла со значением None, параллельно с этим
        инкрементируем переменную size и возвращаем её в конце.
        Returns:
            int: Размер списка.

        """
        current_node = self.head
        size = 0

        while current_node is not None:
            current_node = current_node.next
            size += 1

        return size

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

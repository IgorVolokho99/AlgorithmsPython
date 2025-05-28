"""Модуль, который предоставляет реализацию стандартной структуры двухсвязного списка."""

from typing import Any, Optional, Iterable

from two_linked_list.node import Node


class TwoLinkedList:
    """Класс, который предоставляет реализацию стандартной структуры двухсвязного списка."""

    def __init__(self, iterable: Optional[Iterable[Any]]) -> None:
        """Инициализирует объекты данного класса, задаются два пустыл атрибута head и tail."""
        self.head = None
        self.tail = None

        if Iterable:
            for item in iterable:
                self.push_back(item)

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

        pop_value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return pop_value

    def insert(self, index: int, value: Any) -> None:
        """Метод, вставляющий значение на позицию index.

        Метод, который принимает data, создает объект Node со значением data и вставляет данный узел в позицию index.
        Вызывается исключение IndexError, если указанного индекса не существуетю

        Args:
            index(int): позиция, на которую требуется вставить новый узел.
            value(Any): данные, которые будет содержать новый узел.

        """
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

    def remove(self, value: Any) -> None:
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

    def find(self, value: Any) -> int:
        """Возвращает индекс первого узла со значением data и -1 в случае отсутствия.

        Args:
            value(Any): Значение, по которому будет выполняться поиск.

        Returns:
            int: Индекс первого элемента со значением data и -1 в случае его отсуствия.

        """
        if self.is_empty():
            return -1

        current_node = self.head
        current_index = 0
        while current_node.value != value:
            current_node = current_node.next
            current_index += 1

        if current_node.value != value:
            return -1

        return current_index

    def get(self, index: int) -> Any:
        """Возвращает значение узла по указанному индексу.

        Получает целочисленное значение, являющееся индексом списка и возвращает значение узла, которое находится
        под указанным индексом. В случае, если указанного индекса не существует генерируется исключение.

        Args:
            index(int): Индекс узла значение которого будет возвращено.

        Returns:
            Any:  Значение, которое будет возвращено.

        """
        if index < 0:
            raise IndexError("List indexes must be positive integers")

        current_node = self.head
        i = 0
        while current_node and i < index:
            current_node = current_node.next
            i += 1

        if current_node is None:
            raise IndexError("List index is out of range.")

        return current_node.value

    def set(self, index: int, value: Any) -> None:
        """Добавляет значение value на позицию index в списке.

        Получает целочисленный параметр index, и новое значение узла value.
        Выбрасываются следующие исключения:
        - TypeError, если параметр index не является типом int;
        - ValuError, если index является отрицательным числом;
        - IndeError, если index выходит за пределы максимального индекса.
        В остальных случаях срабатывает сохранение значение value на позицию index в списке.
        Оценка сложности по времени: O(n);
        Оценка сложности по памяти: O(1);

        Args:
            index(int): Позиция, на которую требуется вставить новое значение;
            value(Any): Значение, которое требуется поставить на позицию.

        Examples:
            >>> two_linked_list = TwoLinkedList([1, 2, 3, 4, 5])
            >>> two_linked_list.set(0, 10)
            >>> print(two_linked_list.get(0)) # Выведет 10

        """
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("List indexes must be integer.")
        if index < 0:
            raise ValueError("List indexes must be not negative.")

        current_index = 0
        current_node = self.head
        while current_index < index and current_node:
            current_index += 1
            current_node = current_node.next

        if current_node is None:
            raise IndexError("List index out of range.")
        current_node.value = value

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

    def reverse(self) -> None:
        """Метод, который переворачивает список.

        Оценка сложности по времени: O(n);
        Оценка сложности по памяти: O(1);

        Examples:
            >>> two_linked_list = TwoLinkedList([1, 2, 3, 4, 5])
            >>> two_linked_list.reverse()
            >>> for i in range(two_linked_list.size()):
            ...     print(two_linked_list.get(i)) # -> 5 4 3 2 1

        """
        left, right = self.head, self.tail

        left_index, right_index = 0, self.size() - 1

        while left_index < right_index:
            left.value, right.value = right.value, left.value
            left, right = left.next, right.prev
            left_index += 1
            right_index -= 1

    def clear(self) -> None:
        """Метод, который выполняет очистку двухсвязного списка."""
        while self.head:
            self.pop_back()

    # def extend(self):
    #     pass
    #
    # def __copy__(self):
    #     pass
    #
    # def __deepcopy__(self, memodict={}):
    #     pass
    #
    # def __add__(self, other):
    #     pass
    #
    # def __len__(self):
    #     pass
    #
    # def __str__(self):
    #     pass
    #
    # def __repr__(self):
    #     pass

    def __eq__(self, other) -> bool:  # noqa: ANN001
        """Сравнивает два объекта типа TwoLinkedList.

        Args:
            other(TwoLinkedList): Объект с которым будет происходит сравнение текущего объекта класса.

        Returns:
            bool: True, в случае, если сравниваемые объекты равны и False в противном случае.

        """
        if not isinstance(other, TwoLinkedList):
            return False

        node_1 = self.head
        node_2 = other.head
        while node_1 is not None and node_2 is not None:
            if node_1 != node_2:
                return False
            node_1 = node_1.next
            node_2 = node_2.next

        return True if node_1 is None and node_2 is None else False

    def __reversed__(self) -> None:
        """Магический метод, представляющий из себя генератор для итерирования элементов в обратном порядке.

        Реализация данного метода позволяет передавать объекты функции reversed для итерации по элементам списка в
        обратном порядке.
        Оценка сложности по времени: O(n);
        Оценка сложности по памяти: O(1);

        Examples:
            >>> two_linked_list = TwoLinkedList([1, 2, 3, 4, 5])
            >>> for i in reversed(two_linked_list):
            ...     print(i) # -> 5 4 3 2 1

        Yields:
            Any: Значения узлов списка, начиная с конца.

        """
        current_node = self.tail
        while current_node:
            yield current_node.value
            current_node = current_node.prev

    # def __iter__(self):
    #     pass
    #
    # def __contains__(self, item):
    #     pass
    #
    # def __getitem__(self, item):
    #     pass
    #
    # def __setitem__(self, key, value):
    #     pass
    #
    # def __delitem__(self, key):
    #     pass
    #
    # def __bool__(self):
    #     pass

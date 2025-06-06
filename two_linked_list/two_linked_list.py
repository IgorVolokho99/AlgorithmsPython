"""Модуль, который предоставляет реализацию стандартной структуры двухсвязного списка."""
from copy import deepcopy
from typing import Any, Optional, Iterable

from two_linked_list.node import Node


class TwoLinkedList:
    """Класс, который предоставляет реализацию стандартной структуры двухсвязного списка."""

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """Инициализирует объекты данного класса, задаются два пустыл атрибута head и tail."""
        self.head = None
        self.tail = None

        if iterable:
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
        next_node.prev = new_node

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
        while current_node and current_node.value != value:
            current_node = current_node.next
            current_index += 1

        if not current_node or current_node.value != value:
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
        if not isinstance(index, int):
            raise TypeError("list indices must be integers or slices, not float")
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
        """Метод, который выполняет очистку двухсвязного списка.

        Оценка сложности по времени: O(n);
        Оценка сложности по памяти: O(1);
        """
        while self.head:
            self.pop_back()

    def extend(self, other: "TwoLinkedList") -> None:
        """Присоединяет все элементы другого двусвязного списка к текущему списку.

        Метод проходит по элементам переданного списка `other` от головы до хвоста
        и добавляет каждый элемент в конец текущего списка.
        Оценка сложности по времени: O(n);
        Оценка сложности по памяти: O(n);

        Args:
            other (TwoLinkedList): Другой двусвязный список, элементы которого нужно добавить.

        Examples:
            >>> tll1 = TwoLinkedList([1, 2, 3])
            >>> tll2 = TwoLinkedList([4, 5, 6])
            >>> print(tll2) # [1, 2, 3, 4, 5, 6]

        """
        current_node = other.head
        while current_node:
            self.push_back(current_node.value)
            current_node = current_node.next

    def __copy__(self) -> "TwoLinkedList":
        """Магический метод, создающий поверхностную копию экземпляра класса.

        Возвращает поверхностную копию экземпляра класса. Вызывается функцией copy модуля copy.

        Returns:
            TwoLinkedList: Поверхностная копия объекта.

        """
        new_object = TwoLinkedList()

        for value in self:
            new_object.push_back(value)

        return new_object

    def __deepcopy__(self, memodict: dict = {}) -> "TwoLinkedList":  # noqa: B006
        """Магический метод, создающий глубокую копию экземпляра класса.

        Возвращает глубокую копию экземпляра класса. Вызывается функцией copy модуля copy.

        Returns:
            TwoLinkedList: Глубокая копия экземпляра класса.

        """
        if id(self) in memodict:
            return memodict[id(self)]

        new_object = TwoLinkedList()
        memodict[id(self)] = new_object

        for item in self:
            new_object.push_back(deepcopy(item, memodict))

        return new_object

    def __add__(self, other: "TwoLinkedList") -> "TwoLinkedList":
        """Метод, конкатенирующий два списка.

        Args:
            other(TwoLinkedList): Список, с которым нужно произвести конкатенацию.

        Returns:
            TwoLinkedList: Односвязных список, в котором сначала идут все значения списка self, а потом все значения
            списка other.

        Raises:
            TypeError: Если объект other не является экземпляром класса OneLinkedList.

        """
        if not isinstance(other, TwoLinkedList):
            raise TypeError(f"unsupported operand type(s) for +: 'OneLinkedList' and {type(other)}")

        obj = TwoLinkedList()

        for value in self:
            obj.push_back(value)

        for value in other:
            obj.push_back(value)

        return obj

    def __len__(self) -> int:
        """Магический метод, который возвращает количество узлов в списке и имплементирует работу функции len.

        Returns:
            int: Количество узлов списка.

        """
        return self.size()

    def __str__(self) -> str:
        """Магический метод, который возвращает человекочитабельное представление списка.

        Returns:
            str: Строка вида [1, 2, 3, 4, 5], которая описывает содержимое двухсвязного списка.

        """
        return f"[{', '.join([str(value) for value in self])}]"

    def __repr__(self) -> str:
        """Магический метод, возвращающий "официальное" представление экземпляра класса в виде строки.

        Данный метод позволяет восстановить точную копию экземпляра при помощи функции eval и строки, возвращающейся
        текущим методом.

        Returns:
            str: Официальное представление экземпляра класса.

        """
        return f"TwoLinkedList({str(self)})"

    def __eq__(self, other: "TwoLinkedList") -> bool:  # noqa: ANN001
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

    def __iter__(self) -> Any:
        """Магический метод, который реализует итерацию по экземпляру двухсвязного списка.

        Yields:
            Any: Значения узлов двухсвязного списка.

        Examples:
            >>> two_linked_list = TwoLinkedList([1, 2, 3, 4, 5])
            >>> for value in two_linked_list:
            ...     print(value) # -> 1, 2, 3, 4, 5

        """
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __contains__(self, value: Any) -> bool:
        """Магический метод, проверяющий наличие значения value в списке.

        Реализован при помощи метода find.

        Args:
            value(Any): Искомое значение.

        Returns:
            bool: True, если такой элемент присутствует в списке и False в противном случае.

        """
        return True if self.find(value) != -1 else False

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
            raise ValueError("list indexes must be whole.")
        current_node = self.head
        current_index = 0
        while current_index < index and current_node:
            current_node = current_node.next
            current_index += 1

        if not current_node:
            raise IndexError("List index out of range.")

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
            raise TypeError("list indices must be integers or slices")
        if index < 0:
            raise ValueError("List indexes must be whole.")

        current_node = self.head
        current_index = 0
        while current_index < index and current_node:
            current_node = current_node.next
            current_index += 1

        if current_node is None:
            raise IndexError("List index out of range.")

        current_node.value = value

    def __delitem__(self, index: int) -> None:
        """Магический метод, который имплементирует работу оператора del для удаления по индексу.

        Args:
            index(int): Индекс узла, который нужно удалить.

        """
        if not isinstance(index, int):
            raise TypeError("List indexes must be int.")
        if index < 0:
            raise ValueError("List indexes must by whole.")

        current_node = self.head
        current_index = 0
        while current_index < index and current_node:
            current_node = current_node.next
            current_index += 1

        if current_node is None:
            raise IndexError("List index out of range.")

        if current_node is self.head:
            self.pop_front()
        elif current_node is self.tail:
            self.pop_back()
        else:
            prev_node = current_node.prev
            prev_node.next = current_node.next

    def __bool__(self) -> bool:
        """Магический метод булевых операций.

        Метод, который используется для функции bool и использования экземлпяров класса в булевых выражениях. Реализует
        логику Truthy и Falsy значений.

        Returns:
            bool: True, если значение экземпляра является Truthy и False в противном случае.

        """
        return True if len(self) != 0 else False

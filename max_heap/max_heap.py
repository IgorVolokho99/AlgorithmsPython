"""Модуль, содержащий реализацию двоичной кучи(max-binary-heap)."""
import math


class Heap:
    """Реализация двоичной кучи."""

    def __init__(self) -> None:
        """Инициализирует кучу пустым массивом."""
        self._data = []

    def push(self, number: int) -> None:
        """Добавляет число в кучу.

        Args:
            number(int) : Число, которое будет добавлено в кучу.

        """
        if not (isinstance(number, int) or isinstance(number, float)):
            raise TypeError("Push-value must be an integer or float.")
        index = len(self._data)
        self._data.append(number)
        self._heapify_up(index)

    def _heapify_up(self, index: int) -> None:
        """Проводит "хипизацию" кучи, после добавления нового элемента.

        Элемент под указанным индексом поднимается вверх, покаместь не будет выполнено основное свойство кучи.

        Args:
            index(int) : Позиция с которой нужно провести хипизацию вверх;

        """
        if (index - 1) // 2 >= 0 and self._data[index] > self._data[(index - 1) // 2]:
            self._data[index], self._data[(index - 1) // 2] = self._data[(index - 1) // 2], self._data[index]
            self._heapify_up((index - 1) // 2)

    def pop(self) -> int:
        """Возвращает и удаляет максимальный элемент кучи.

        Меняет местами первый и последний элемент кучи, запоминает и удаляет максимальный элемент, который попал в конец
        списка. Проводится хипизация кучи вниз для корневого элемента.

        Returns:
            int: Максимальный элемент кучи.

        """
        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        return_value = self._data.pop()
        self._heapify_down(0)
        return return_value

    def _heapify_down(self, index: int) -> None:
        """Проводит "хипизацию" кучи, после добавления нового элемента.

        Элемент под указанным индексом опускается вниз, покаместь не будет выполнено основное свойство кучи.

        Args:
            index(int) : Позиция с которой нужно провести хипизацию вверх;

        """
        while index * 2 + 2 < len(self._data):
            if self._data[index * 2 + 1] > self._data[index * 2 + 2]:
                new_index = index * 2 + 1
            else:
                new_index = index * 2 + 2
            if self._data[index] < self._data[new_index]:
                self._data[index], self._data[new_index] = self._data[new_index], self._data[index]
                index = new_index
            else:
                break

        if index * 2 + 1 < len(self._data):
            new_index = index * 2 + 1
            if self._data[index] < self._data[new_index]:
                self._data[index], self._data[new_index] = self._data[new_index], self._data[index]

    def peek(self) -> int:
        """Возвращает самое большое число в куче.

        Returns:
            int: Самое большое число кучи, стоящее на вершине.

        """
        return self._data[0]

    def is_empty(self) -> bool:
        """Проводит проверку пустоты кучи.

        Returns:
            bool: True, если куча пустая и False в противном случае.

        """
        return True if len(self._data) == 0 else False

    def clear(self) -> None:
        """Удаляет все узлы в куче."""
        self._data.clear()

    def depth(self) -> int:
        """Возвращает глубину кучи.

        Returns:
            int: Глубина кучи, количество уровней на которые заполненна куча полностью или частично.

        """
        if len(self._data) == 0:
            return 0

        return int(math.log2(len(self._data))) + 1

    def __len__(self) -> int:
        """Возвращает количество узлов кучи.

        Returns:
            int: Количество узлов кучи.

        """
        return len(self._data)

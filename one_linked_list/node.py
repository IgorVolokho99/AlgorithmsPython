"""Модуль, содержащий реализацию Node."""

from typing import Any


class Node:
    """Класс, реализующий в себе логику узлов односвязного списка."""

    def __init__(self, value: Any = None):
        """Конструктор класса Node.

        :param value: Необязательный параметр value любого типа.
        """
        self.value = value
        self.next = None

    def __eq__(self, other: Any) -> bool:
        """Магический метод equal, испольщующий для сравнения двух экземпляров класса Node.

        Проверяет на значение и тип атрибута value двух экземпляров класса.

        Args:
            other: Объект, с котором будет происходить сравнение.

        Returns:
            bool: True, в случае равенства объектов и False в противном случае..

        """
        if not isinstance(other, Node) or not isinstance(self.value, type(other.value)) or self.value != other.value:
            return False
        return True

"""Модуль, содержащий реализацию Node."""

from typing import Any


class Node:
    """Класс Node, реализующий в себе логику узлов односвязного списка."""

    def __init__(self, value: Any = None):
        """Конструктор класса Node.

        :param value: Необязательный параметр value любого типа.
        """
        self.value = value
        self.next = None

"""Модуль, содержащий реализацию узлов для двухсвязного списка."""

from typing import Any


class Node:
    """Класс, реализующий в себе логику узлов двухсвязного списка."""

    def __init__(self, value: Any):
        """Инициализирует объекты данного типа(узел двухсвязного списка).

        Принимает value, которое может являться значением любого типа и сохраняет его в атрибут value. Также создаются
        атрибуты next и prev, которые будут выступать в роли указателей на соседние узлы.

        Args:
            value(Any): Значение любого типа.

        """
        self.value = value
        self.next = None
        self.prev = None

    def __eq__(self, other) -> bool: # noqa: ANN001
        """Сравнивает два объекта типа Node. Сравнение ведется только по атрибуту value.

        Args:
            other: Объект типа Node с которым происходит сравнение текущего объекта.

        Returns:
            bool: True, если объекты равны и False в противеом случае.

        """
        if not isinstance(other, Node):
            return False
        return True if isinstance(self.value, type(other.value)) and self.value == other.value else False

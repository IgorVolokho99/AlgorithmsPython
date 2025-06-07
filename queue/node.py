"""Модуль, который содержит вспомогательный класс Node для реализации структуры данных Queue."""

from typing import Any


class Node:
    """Класс, содержащий реализацию узлов для очереди."""

    def __init__(self, value: Any, next_node: "Node" = None) -> None:
        """Инициализирует экземпляр класса Node.

        Args:
            value(Any): Значение, которое будет содержать узел;
            next_node(Node): Указатель на следующий узел в стеке.

        """
        self.value = value
        self.next_node = next_node

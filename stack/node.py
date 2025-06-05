"""Модуль, содержащий реализацию узлов для стека."""
from typing import Any


class Node:
    """Класс, содержащий реализацию узлов для стека."""

    def __init__(self, value: Any, next_node: "Node" = None) -> None:
        """Инициализирует экземпляр класса Node.

        Args:
            value(Any): Значение, которое будет содержать узел;
            next_node(Node): Указатель на следующий узел в стеке.

        """
        self.value = value
        self.next_node = next_node

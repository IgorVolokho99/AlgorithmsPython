"""Модуль, содержащий реализацию узлов для двухсвязного списка."""

from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None
        self.prev = None

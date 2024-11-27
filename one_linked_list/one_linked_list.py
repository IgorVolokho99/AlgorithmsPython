from typing import Any

from node import Node


class OneLinkedList:
    def __init__(self, node: Node = None):
        self.head = node
        self.tail = node

    def append(self, data: Any) -> None:
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next




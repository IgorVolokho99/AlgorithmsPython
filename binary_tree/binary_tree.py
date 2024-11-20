from typing import Union

from node import Node


class BinaryTree:
    def __init__(self):
        self.root = None
        self.depth = 0

    def is_empty(self):
        return True if self.root is None else False

    def __find(self, node: Node, parent: Union[Node, None], value: int) -> tuple:
        if node is None:
            return None, parent, False

        if value == node.value:
            return node, parent, True

        if value < node.value:
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.value:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, value: int) -> Node:
        obj = Node(value)
        if self.is_empty():
            self.root = obj
            return obj

        n, p, fl_find = self.__find(self.root, None, obj.value)

        if not fl_find and n:
            if obj.value < n.value:
                n.left = obj
            else:
                n.right = obj

        self.calculate_depth(self.root, 1)
        return obj

    def show_tree(self, node: Node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.value)
        self.show_tree(node.right)

    def __del_leaf(self, node, parent):
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    def __del_one_child(self, node, parent):
        if parent.left == node:
            if node.left is None:
                parent.left = node.right
            else:
                parent.left = node.left
        else:
            if node.left is None:
                parent.right = node.right
            else:
                parent.right = node.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def del_node(self, value: int):
        n, p, fl_find = self.__find(self.root, None, value)

        if not fl_find:
            return None

        if n.left is None and n.right is None:
            self.__del_leaf(n, p)
        elif n.left is None or n.right is None:
            self.__del_one_child(n, p)
        else:
            node, parent = self.__find_min(n.right, n)
            n.value = node.value
            self.__del_one_child(node, parent)

    def __contains__(self, item: int):
        if self.is_empty():
            return False
        else:
            return self.find(item, self.root)

    def find(self, value: int, node: Node):
        if node is None:
            return False

        if node.value == value:
            return True
        else:
            return self.find(value, node.left) if value < node.value else self.find(value, node.right)

    def calculate_depth(self, node: Node, depth: int = 0):
        if node is None:
            if depth > self.depth:
                self.depth = depth
            return
        self.calculate_depth(node.left, depth + 1)
        self.calculate_depth(node.right, depth + 1)

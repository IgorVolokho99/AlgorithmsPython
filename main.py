import copy

from one_linked_list.one_linked_list import OneLinkedList
from two_linked_list.two_linked_list import TwoLinkedList
from collections import deque


def main():
    obj = TwoLinkedList([1, 2, 3, 4, 5])
    print(copy.copy(obj))
    d = deque([1, 2, 3, 4, 5])

    print(d.popleft())
    print(d)


if __name__ == "__main__":
    main()

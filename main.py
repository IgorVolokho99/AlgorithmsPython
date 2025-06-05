import copy

from one_linked_list.one_linked_list import OneLinkedList
from two_linked_list.two_linked_list import TwoLinkedList


def main():
    obj = TwoLinkedList([1, 2, 3, 4, 5])
    print(copy.copy(obj))


if __name__ == "__main__":
    main()

from one_linked_list.one_linked_list import OneLinkedList
from copy import copy, deepcopy


def main():
    obj = OneLinkedList([1, 2, 3])

    for item in obj:
        print(item)

    s = repr(obj)

    obj2 = eval(s)

    for item in obj2:
        print(item)

if __name__ == "__main__":
    main()

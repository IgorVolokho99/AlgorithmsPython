from one_linked_list.one_linked_list import OneLinkedList
from copy import copy, deepcopy


def main():
    obj = OneLinkedList()
    obj.push_back(1)
    obj.push_back(2)
    obj.push_back(3)
    obj.push_back(4)
    obj.push_back([1, 2, 3])

    obj2 = copy(obj)

    obj[4][1] = 1232

    for item in obj2:
        print(item)


if __name__ == "__main__":
    main()

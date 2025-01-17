from one_linked_list.one_linked_list import OneLinkedList


def main():
    obj = OneLinkedList()
    obj.push_back(1)
    obj.push_back(2)
    obj.push_back(3)
    obj.push_back(4)
    obj.push_back(5)

    obj2 = OneLinkedList()
    obj2.push_back(1)
    obj2.push_back(2)
    obj2.push_back(3)
    obj2.push_back(4)
    obj2.push_back(5)
    obj2.push_back(6)

    print(obj == obj2)


if __name__ == "__main__":
    main()

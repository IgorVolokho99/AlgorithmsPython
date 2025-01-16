from one_linked_list.one_linked_list import OneLinkedList


def main():
    obj = OneLinkedList()
    obj.push_back(1)
    obj.push_back(1)
    obj.push_back(1)
    obj.push_back(1)

    print(len(obj))
    print(obj.size())
    print(obj)

    obj2 = OneLinkedList()
    obj2.push_front(2)
    print(obj2)


if __name__ == "__main__":
    main()

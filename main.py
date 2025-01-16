from one_linked_list.one_linked_list import OneLinkedList


def main():
    obj = OneLinkedList()
    obj.push_back(1)
    obj.push_back(2)
    obj.push_back(3)
    obj.push_back(4)
    obj.push_back(5)

    print(obj)
    obj.reverse()
    print(obj)


if __name__ == "__main__":
    main()

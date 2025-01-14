from one_linked_list.one_linked_list import OneLinkedList


def main():
    obj = OneLinkedList()
    obj.push_back(1)
    obj.push_back(5)
    obj.push_back(1)
    obj.push_back(2)

    obj.set(-1, "A")

    obj.show()


if __name__ == "__main__":
    main()

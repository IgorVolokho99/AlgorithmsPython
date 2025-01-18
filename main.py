from one_linked_list.one_linked_list import OneLinkedList


def main():
    obj = OneLinkedList()
    obj.push_back(1)
    obj.push_back(2)
    obj.push_back(3)
    obj.push_back(4)
    obj.push_back(5)

    obj2 = OneLinkedList()
    obj2.push_back(15)
    obj2.push_back(17)

    obj3 = obj + 2

    for item in obj3:
        print(item)



if __name__ == "__main__":
    main()

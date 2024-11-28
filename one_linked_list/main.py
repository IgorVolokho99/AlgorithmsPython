from one_linked_list import OneLinkedList


def main():
    obj = OneLinkedList()
    obj.push_back(1)
    obj.push_back(5)
    obj.push_back(2)

    print(obj.pop_back())
    print(obj.pop_back())
    print(obj.pop_back())
    print(obj.pop_back()) # Error


if __name__ == "__main__":
    main()

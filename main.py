from one_linked_list.one_linked_list import OneLinkedList
from two_linked_list.two_linked_list import TwoLinkedList


def main():
    obj = TwoLinkedList()

    obj.push_back(2)
    obj.push_back(2)
    obj.push_back(2)

    print(obj.head.value)
    print(obj.head.next.value)
    print(obj.head.next.next.value)


if __name__ == "__main__":
    main()

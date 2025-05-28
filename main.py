from one_linked_list.one_linked_list import OneLinkedList
from two_linked_list.two_linked_list import TwoLinkedList


def main():
    obj = TwoLinkedList([1, 2, 3, 4, 5])
    obj2 = TwoLinkedList([1, 2, 3, 4, 5][::-1])
    obj.reverse()

    print(obj == obj2)

    for i in range(obj.size()):
        print(obj.get(i))


if __name__ == "__main__":
    main()

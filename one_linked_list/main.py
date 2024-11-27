from one_linked_list import OneLinkedList


def main():
    obj = OneLinkedList()
    obj.append(1)
    obj.append(5)
    obj.append(2)

    print(obj.head.next.next.value)


if __name__ == "__main__":
    main()

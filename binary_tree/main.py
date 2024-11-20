from binary_tree import BinaryTree


def main():
    b = BinaryTree()
    b.append(5)
    b.append(1)
    b.append(7)
    b.append(4)
    b.append(3)
    b.append(9)
    b.append(8)
    b.append(18)
    b.append(-5)
    b.append(20)

    x = 5
    print(x in b)
    b.del_node(x)
    print(x in b)


if __name__ == "__main__":
    main()

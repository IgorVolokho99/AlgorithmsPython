from max_heap import Heap


def main():
    max_heap = Heap([5, 2, 10, 51, 1, 2])

    print(max_heap.depth())
    print(max_heap.peek())
    print(max_heap.peek())
    print(max_heap.pop())
    print(max_heap.peek())


if __name__ == "__main__":
    main()

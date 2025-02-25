class TwoLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        """Метод, проверяющий является ли список пуст.

        Returns:
            bool: True, если список пуст и False в противном случае.

        """
        return self.head is None


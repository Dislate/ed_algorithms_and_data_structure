from nodes import Node


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def __iter__(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def append(self, data):
        node = Node(data)

        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        for node in self:
            if data == node:
                return True
        return False

    def clear(self):
        """Clear the entire list."""
        self.tail = None
        self.head = None
        # My fix for size
        self.size = 0
        """
        My solution for clearing a Singly Linked List. 
        This initializes the new object and clears all old nodes from memory, since old nodes have no references.
        self.__init__()
        """


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)

    for num in sll:
        print(num)
    print(sll.size)  # 3
    sll.append(5)
    print(sll.size)  # 4
    sll.delete(5)
    print(sll.search(2))  # True
    print(sll.search(5))  # False
    sll.clear()
    print(sll.size) # 0

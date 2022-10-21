class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        print(self.data)


if __name__ == "__main__":
    # Init nodes
    n1, n2, n3 = Node('eggs'), Node('ham'), Node('spam')
    # Linking nodes
    n1.next = n2
    n2.next = n3

    # Set current node
    current = n1
    # Searching the structure in depth
    while current:
        print(current.data)
        current = current.next

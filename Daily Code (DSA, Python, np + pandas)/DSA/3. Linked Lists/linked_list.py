class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        # Private attribute - don't modify it from outside.
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        nodes = []
        curr = self.head
        while curr:
            # O/P always should be string for better formatting.
            nodes.append(str(curr.data))
            curr = curr.next

        return "->".join(nodes) if nodes else "Empty list"

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next


    def insert_at_start(self, data):
        node = Node(data)

        node.next = self.head
        self.head = node

    def inset_at_end(self, data):
        node = Node(data)

        # Missed if head is None also following loop can be simplified.
        # while True:
        #     if curr.next:
        #         curr = curr.next
        #     else:
        #         node.next = curr.next
        #         curr.next = node

        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = node

    @staticmethod
    def insert_after(prev, data):
        node = Node(data)

        if not prev: raise ValueError

        node.next = prev.next
        prev.next = node

    def delete_first(self):
        if not self.head:
            return None

        curr = self.head
        removed = curr.data
        self.head = curr.next
        self._size -= 1

        return removed



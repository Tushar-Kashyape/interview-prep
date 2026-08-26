class Node:
    def __init__(self, data):
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
        pass

    def inset_at_end(self, data):
        pass



    def insert_after(prev, data):
        pass


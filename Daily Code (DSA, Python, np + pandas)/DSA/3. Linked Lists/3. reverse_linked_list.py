from linked_list import Node

def reverse_linked_list(head: Node) -> Node | None:
    curr, prev = head, None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
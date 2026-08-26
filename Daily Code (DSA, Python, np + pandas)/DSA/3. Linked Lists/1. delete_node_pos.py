from linked_list import Node

def delete_node(head: Node, pos) -> Node:
    """
    Deletes the node at the specified 0-based index.
    Returns the new head node.
    Raises IndexError if index is negative or out of bounds.
    """
    if pos < 0 or not head:
        raise IndexError(f"{pos} is invalid")

    if pos == 0:
        new_head = head.next
        head.next = None
        return new_head

    temp, prev, count = head, None, 0
    while temp and count != pos:
        prev = temp
        temp = temp.next
        count += 1

    if temp:
        prev.next = temp.next
        temp.next = None
        return head
    else:
        raise IndexError(f"Index {pos} out of bounds of linked list")
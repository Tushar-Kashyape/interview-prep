from linked_list import Node

def delete_node_by_val(head: Node, target) -> Node | None:
    """
    Deletes all nodes with data matching target from the linked list.
    Returns the updated head node.
    """
    if not head:
        return None

    curr, prev = head, None

    while curr:
        if curr.data == target:
            if not prev:
                head = curr.next
            else:
                prev.next = curr.next
        else:
            prev = curr

        curr = curr.next

    return head
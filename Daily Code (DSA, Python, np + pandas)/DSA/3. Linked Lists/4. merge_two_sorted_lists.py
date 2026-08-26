from linked_list import Node

def merge_two_lists(list1: Node, list2: Node) -> Node:
    if not list1: return list2

    if not list2: return list1

    merged = curr = Node()

    while list1 and list2:

        if list1.data < list2.data:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    curr.next = list1 or list2

    return merged.next

"""
After successful submission, found out there is scope for optimization through
recursion. Tried to write it down by myself:
"""

def merge_list_recursively(list1: Node, list2: Node) -> Node:
    if not list1: return list2

    if not list2: return list1

    if list1.data < list2.data:
        list1.next = merge_list_recursively(list1.next, list2)

        return list1
    else:
        list2.next = merge_list_recursively(list1, list2.next)

        return list2
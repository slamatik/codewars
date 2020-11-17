class Node:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next


def search_k_from_end(linked_list, k):
    dummy = Node(0, linked_list)
    left_pointer = right_pointer = dummy
    try:
        for i in range(k):
            right_pointer = right_pointer.next
        while right_pointer.next:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
    except AttributeError:
        return None

    left_pointer = left_pointer.next
    return left_pointer.data

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        # For easier debugging / printing
        return f'{self.val} -> {self.next}'

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next
    
    # Append the remaining nodes
    current.next = list1 if list1 else list2
    return dummy.next


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])

print(merge_two_lists(list1, list2))
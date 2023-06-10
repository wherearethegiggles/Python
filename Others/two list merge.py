class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode(0)  # Dummy node to simplify the merging process
    current = dummy  # Pointer to the current node in the merged list

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining nodes of the non-empty list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next  # Return the head of the merged list
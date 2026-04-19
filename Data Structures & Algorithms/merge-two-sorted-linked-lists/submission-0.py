# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2

        if not t1:
            return t2

        if not t2:
            return t1

        head = ListNode(0)
        t = head
        while t1 and t2:
            if t1.val < t2.val:
                t.next = t1
                t1 = t1.next
            else:
                t.next = t2
                t2 = t2.next
            t = t.next

        if t1:
            t.next = t1
        else:
            t.next = t2
        return head.next
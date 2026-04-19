# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = 0
        t1 = head
        while t1 and c < k:
            t1 = t1.next
            c += 1

        if c < k:
            return head
        
        i = 0
        p = None
        n = None
        t = head

        while t and i < k:
            n = t.next
            t.next = p
            p = t
            t = n
            i += 1
        if t:
            head.next = self.reverseKGroup(t, k)
        return p
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, head):
        p = None
        t = head
        while t:
            n = t.next
            t.next = p
            p = t
            t = n
        return p

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        f = l1
        s = l2

        head = None
        temp = None
        carry = 0

        while f or s or carry:
            fdata = f.val if f is not None else 0
            sdata = s.val if s is not None else 0

            sum = fdata + sdata + carry

            carry = sum // 10
            digit = sum % 10

            node = ListNode(digit)
            if head is None:
                head = node
                temp = node
            else:
                temp.next = node
                temp = temp.next
            
            if f:
                f = f.next
            if s:
                s = s.next

        return head
            



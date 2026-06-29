# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        cur1, cur2 = l1, l2
        carry = 0

        while cur1 or cur2 or carry:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0

            total = v1 + v2 + carry
            val = total % 10
            carry = total // 10

            node.next = ListNode(val)
            node = node.next

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

        return dummy.next

            
            
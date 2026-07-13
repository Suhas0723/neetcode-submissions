
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = head
        length = 0
        while p1 is not None:
            length += 1
            p1 = p1.next

        p2 = dummy
        for i in range(length - n):
            p2 = p2.next

        p2.next = p2.next.next


        return dummy.next

        
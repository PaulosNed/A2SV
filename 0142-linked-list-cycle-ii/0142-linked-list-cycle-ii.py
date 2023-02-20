class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        first = True
        start = head
        intercept = None
        while(fast and fast.next):
            if not first and fast == slow:
                intercept = fast
                break
            first = False
            fast = fast.next.next
            slow = slow.next
        if  not fast or not fast.next:
            return None
        while(start != intercept):
            start = start.next
            intercept = intercept.next
        return start       
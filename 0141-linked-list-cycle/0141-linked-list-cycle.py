# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        first = True
        while(fast and fast.next):
            if not first and fast == slow:
                return True
            first = False
            fast = fast.next.next
            slow = slow.next
        return False
            
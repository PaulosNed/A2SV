# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        fast = head
        slow = head
        twins = [head.val]
        while(fast.next.next):
            slow = slow.next
            fast = fast.next.next
            twins.append(slow.val)
        slow = slow.next
        while(slow):
            currTwin = twins.pop()
            ans = max(ans, currTwin+slow.val)
            slow = slow.next
        return ans
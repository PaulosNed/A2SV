# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        final = head
        while(head):
            sz += 1 
            head = head.next
        head = final
        if sz == n:
            return final.next
        for _ in range(sz-n-1):
            head = head.next
        head.next = head.next.next
        return final
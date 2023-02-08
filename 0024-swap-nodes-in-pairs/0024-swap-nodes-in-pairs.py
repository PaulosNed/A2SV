# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        final = ListNode()
        final.next = head
        head = final
        while(head.next and head.next.next):
            nxt = head.next.next
            head.next.next = head.next.next.next
            nxt.next = head.next
            head.next = nxt
            head = head.next.next
        return final.next
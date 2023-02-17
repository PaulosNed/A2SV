# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        head = dummy
        for i in range(left-1):
            head = head.next
        initial = head
        head = head.next
        last = head
        head = head.next
        prev = last
        for _ in range(right-left):
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        initial.next = prev
        last.next = head
        return dummy.next
            
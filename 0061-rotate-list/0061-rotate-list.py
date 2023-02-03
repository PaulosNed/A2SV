# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        if not head or not head.next:
            return head
        count = 0
        while(head):
            count += 1
            head = head.next
        head = dummy.next
        for _ in range(k%count):
            while(head.next.next):
                head = head.next
            curr = head.next
            head.next = None
            curr.next = dummy.next
            dummy.next = curr
            head = dummy.next
        return dummy.next
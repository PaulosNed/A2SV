# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"))
        dummy.next = head
        while(head.next):
            if head.next.val < head.val:
                curr = head.next
                head.next = head.next.next
                initial = dummy
                while(initial.next.val < curr.val):
                    initial = initial.next
                curr.next = initial.next
                initial.next = curr
            else:
                head = head.next
        return dummy.next
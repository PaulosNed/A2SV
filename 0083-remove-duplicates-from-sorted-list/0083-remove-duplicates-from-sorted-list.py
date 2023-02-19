# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = set()
        dummy = ListNode()
        dummy.next = head
        head = dummy
        while(head.next):
            while(head.next.val in vals):
                head.next = head.next.next
                if head.next == None:
                    return dummy.next
            vals.add(head.next.val)
            head = head.next
        return dummy.next
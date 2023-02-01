# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = ListNode()
        final = dummy
        dummy.next = head
        while(dummy.next):
            if dummy.next.val >= x:
                break
            dummy = dummy.next
        curr = dummy
        while(dummy.next):
            if dummy.next.val < x:
                edit = dummy.next
                dummy.next = dummy.next.next
                edit.next = curr.next
                curr.next = edit
                curr = curr.next
            else:
                dummy = dummy.next
        return final.next
        
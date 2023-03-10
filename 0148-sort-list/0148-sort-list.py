# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while(head):
            vals.append(head.val)
            head = head.next
        
        vals.sort()
        final = ListNode()
        head = final
        for val in vals:
            head.next = ListNode(val)
            head = head.next
        
        return final.next
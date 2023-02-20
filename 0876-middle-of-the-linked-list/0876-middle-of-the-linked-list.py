# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 1
        initial = head
        while(head.next != None):
            size+=1
            head = head.next
        limit = (size//2) 
        head = initial
        for _ in range(limit):
            head = head.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        head = ListNode()
        final = head
        while l1 !=None or l2 != None:
            if l1 == None:
                tot = l2.val+rem
            elif l2 == None:
                tot = l1.val+rem
            else:
                tot = l1.val + l2.val + rem
            if rem:
                rem-=1
            if tot >= 10:
                rem += 1
                tot -= 10
            head.next = ListNode(tot)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            head = head.next
        if rem:
            head.next = ListNode(rem)
        return final.next
            
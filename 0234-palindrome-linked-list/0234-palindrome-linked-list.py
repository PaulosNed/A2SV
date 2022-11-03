# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while(head != None):
            vals.append(head.val)
            head = head.next
        start = 0
        end = len(vals) - 1
        while start < end:
            if vals[start] != vals[end]:
                return False
            start+=1
            end-=1
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        size = 0
        stack = []
        vals = []
        while(head != None):
            vals.append(head.val)
            size+=1
            head = head.next
        final = [0] * size
        for i,v in enumerate(vals):
            while stack and stack[-1][1] < v:
                idx, val = stack.pop()
                final[idx] = v
            stack.append([i,v])
        return final
        
        
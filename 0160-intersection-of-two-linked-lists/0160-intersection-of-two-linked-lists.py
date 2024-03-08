# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        setB = set()
        
        while headA or headB:
            if headA in setB or headA == headB:
                return headA
            
            if headB in setA:
                return headB
            
            setA.add(headA)
            setB.add(headB)
            headA = headA.next if headA else None
            headB = headB.next if headB else None
        
        return None
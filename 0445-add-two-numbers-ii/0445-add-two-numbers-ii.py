# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            
            if head == None or head.next == None:
                return head
            
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
        
            return prev
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
    
        rem = 0
        ans_reversed = ListNode()
        head = ans_reversed
        
        while l1 or l2 or rem:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            sum_ = val1 + val2 + rem
            rem = 0
            if sum_ >= 10:
                rem = (sum_ - (sum_ % 10)) // 10
                head.next = ListNode(sum_ % 10)
                
            else:
                head.next = ListNode(sum_)
                
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            head = head.next
        
        return reverseList(ans_reversed.next)
            
            
            
            
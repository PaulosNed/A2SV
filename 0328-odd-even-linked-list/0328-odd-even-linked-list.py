# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odds = head
        head = head.next
        evens = head
        firstOdd = odds
        firstEven = evens
        head = head.next
        curr = True
        while(head):
            nxt = head.next
            if curr:
                odds.next = head
                odds = odds.next
                curr = False
            else:
                evens.next = head
                evens = evens.next
                curr = True
            head = nxt
        if curr:
            odds.next = None
        else:
            evens.next = None
        odds.next = firstEven
        return firstOdd
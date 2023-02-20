# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        final = ListNode(0, head)
        if head == None or head.next == None:
            return head
        final.next = head
        prev = final
        duplicate = False
        while True:
            while head.next and head.val == head.next.val:
                duplicate = True
                if head.next.next:
                    head.next = head.next.next
                else:
                    prev.next = None
                    return final.next
                
            if not duplicate:
                prev.next = head
                prev = head
            else:
                duplicate = False
                
            if head.next:
                head = head.next
            else:
                return final.next
        
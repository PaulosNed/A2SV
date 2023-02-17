# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        if(list1.val < list2.val):
            head = list1
            list1= list1.next
        else:
            head = list2
            list2 = list2.next
        final = head
        while(list1 != None or list2 != None):
            if list1 == None:
                head.next = list2
                head = head.next
                list2 = list2.next
            elif list2 == None:
                head.next = list1
                head = head.next
                list1 = list1.next
            elif list1.val <= list2.val:
                head.next = list1
                head = head.next
                list1 = list1.next
            else:
                head.next = list2
                head = head.next
                list2 = list2.next
        return final
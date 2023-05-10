# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedHeap = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heappush(sortedHeap, head.val)
                head = head.next
        
        ans = []
        while sortedHeap:
            ans.append(heappop(sortedHeap))
            
        final = ListNode()
        head = final
        for a in ans:
            head.next = ListNode(a)
            head = head.next
        
        return final.next
                
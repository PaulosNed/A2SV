class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        citations.reverse()
        
        while(left <= right):
            mid = left + ((right-left) // 2)
            
            if mid < citations[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
        return left
            
        
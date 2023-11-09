class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        def findValue(mid):
            return arr[mid] - 1 - mid
        
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            val = findValue(mid)
            
            if findValue(mid) < k:
                start = mid + 1
            
            else:
                end = mid - 1
        
        
        return arr[end] + (k - findValue(end))
        
        
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        start = 0
        end = 0
        
        while end <  len(arr):
            if end - start == 3:
                return True
            
            if arr[end] % 2 == 0:
                start = end + 1
            
            end += 1
        
        if end - start == 3:
            return True
        
        return False
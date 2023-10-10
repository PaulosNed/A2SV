class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def search(house):
            start = 0
            end = len(heaters) - 1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                if heaters[mid] < house:
                    start = mid + 1
                
                elif heaters[mid] > house:
                    end = mid - 1
                
                else:
                    return 0
            
            ans = float("inf")
            
            if end >= 0:
                ans = house - heaters[end]
            
            if start < len(heaters):
                ans = min(ans, heaters[start] - house)
            
            return ans
        
        ans = 0
        
        heaters.sort()
        
        for house in houses:
            ans = max(ans, search(house))
        
        return ans
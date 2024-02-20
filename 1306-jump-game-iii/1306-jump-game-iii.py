class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = set()
        
        @cache
        def dp(idx):
            if idx < 0 or idx >= len(arr) or idx in visited:
                return False
            
            visited.add(idx)
            if arr[idx] == 0:
                return True
            
            return dp(idx + arr[idx]) or dp(idx - arr[idx])
        
        return dp(start)
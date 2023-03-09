class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        
        def backtrack(arr):
            
            if len(arr) == k:
                output.append(arr)
                return
            
            for j in range(arr[-1] + 1, n+1):
                    backtrack(arr + [j])
            
        for i in range(1, n+1):
            backtrack([i])
        return output
                    
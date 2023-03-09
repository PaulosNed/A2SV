class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        arr = []
        
        def backtrack():
            if len(arr) == k:
                output.append(arr[:])
                return
            
            start = 1 if not arr else arr[-1] + 1
            for j in range(start, n+1):
                arr.append(j)
                backtrack()
                arr.pop()
            return
        
        backtrack()
        return output
                    
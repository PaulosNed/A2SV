class Solution:
    def maxLength(self, arr: List[str]) -> int:
        length = 0
        
        def backtrack(curr, idx, checker):
            nonlocal length
            
            if curr:
                currChecker = set()
                for item in curr[-1]:
                    if item in checker or item in currChecker:
                        final = "".join(curr[:-1])
                        length = max(length, len(final))
                        return
                    currChecker.add(item)
                checker = checker | currChecker
            
            for i in range(idx, len(arr)):
                curr.append(arr[i])
                backtrack(curr, i+1, checker)
                curr.pop()
            
            final = "".join(curr)
            length = max(length, len(final))
                        
        backtrack([], 0, set())
        return length
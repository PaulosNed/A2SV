class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        
        def backtrack(curr):
            nonlocal count
            
            
            if curr and curr[-1] % (len(curr)) != 0 and (len(curr)) % curr[-1]!= 0:
                return
            
            if len(curr) == n:
                count += 1
                return
            
            temp = set(curr)
            for i in range(1, n + 1):
                if i in temp:
                    continue
                curr.append(i)
                backtrack(curr)
                curr.pop()
        
        backtrack([])
        return count
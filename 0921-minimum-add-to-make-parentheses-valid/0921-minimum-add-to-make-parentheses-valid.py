class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        cnt = 0
        stack = []
        
        for l in s:
            if l == "(":
                cnt += 1
                stack.append("(")
            
            else:
                if stack:
                    cnt -= 1
                    stack.pop()
                
                else:
                    cnt += 1
        
        return cnt
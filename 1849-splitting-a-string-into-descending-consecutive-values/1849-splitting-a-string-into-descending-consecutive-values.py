class Solution:
    def splitString(self, s: str) -> bool:
        selected = []
        
        def backtrack(idx):
            
            if idx >= len(s):
                return len(selected) >= 2
            
            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                if not selected or selected[-1] - val == 1:
                    selected.append(val)
                    if backtrack(i+1):
                        return True
                    selected.pop()
                
        return backtrack(0)
            
            
                
            
class Solution:
    def numDecodings(self, s: str) -> int:
        
        count = 0

        @cache
        def backtrack(curr, idx):
            if curr and (not 1 <= int(curr) <= 26):
                return 0
            
            if curr and curr[0] == '0':
                return 0
            
            if idx >= len(s):
                return 1
            
            ans = 0
            for i in range(idx, len(s)):
                curr = s[idx:i+1]
                ans += backtrack(curr, i+1)
                
            return ans

        return backtrack(None, 0)
        
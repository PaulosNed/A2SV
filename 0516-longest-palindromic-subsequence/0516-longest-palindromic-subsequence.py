class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_reversed = ''.join(list(reversed(s)))
        # print(s_reversed)
        
        @cache
        def dp(i, j):
            if i >= len(s) or j >= len(s):
                return 0
            
            if s[i] == s_reversed[j]:
                return 1 + dp(i + 1, j + 1)
            
            else:
                opt1 = dp(i + 1 , j)
                opt2 = dp(i, j + 1)
                
                return max(opt1, opt2)
        
        return dp(0, 0)
            
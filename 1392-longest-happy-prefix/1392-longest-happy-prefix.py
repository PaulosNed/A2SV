class Solution:
    def longestPrefix(self, s: str) -> str:
        
        lsp = [0] * len(s)
        
        i = 0
        j = 1
        
        while j < len(s):
            if s[i] == s[j]:
                lsp[j] = i + 1
                i += 1
                j += 1
            
            else:
                if i == 0:
                    j += 1
                
                else:
                    i = lsp[i - 1]
        
        length = lsp[-1]
        
        return s[:length]
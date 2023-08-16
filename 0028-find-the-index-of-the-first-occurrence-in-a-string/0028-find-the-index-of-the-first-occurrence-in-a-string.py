class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        start = 0
        end = len(needle)
        
        while end <= len(haystack):
            if haystack[start:end] == needle:
                ans = start
                break
            
            start += 1
            end += 1
        
        return ans
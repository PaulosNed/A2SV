class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        start = 0
        end = 0
        s = str(s)
        
        while end < len(s):
            
            if end - start == k:
                # print(s[start], s[end], start, end, s[:start], s[end:])
                s = s[:start] + s[end:]
                start = max(0, start - k - 1)
                end = start
                # print(s[start], start, s, s[end], end)
                
            elif s[start] == s[end]:
                end += 1
            
            else:
                start = end
        
        if end - start == k:
            s = s[:start] + s[end:]
            start = max(0, start - k - 1)
            end = start

        return s
            
            
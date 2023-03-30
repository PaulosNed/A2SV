class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid = []
        
        
        def backtrack(start, end, curr):
            if curr and (not 0 <= int(curr[-1]) <= 255):
                return
            
            if curr and len(curr[-1]) > 1 and curr[-1][0] == "0":
                return
            
            if end > len(s):
                if len(curr) == 4:
                    valid.append(curr[:])
                return
            
            while end <= len(s):
                curr.append(s[start:end])
                backtrack(end, end+1, curr)
                curr.pop()
                end += 1
        
        backtrack(0, 1, [])
        
        final = []
        for v in valid:
            final.append(".".join(v))
            
        return final
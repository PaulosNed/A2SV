class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 1:
            if s.isdigit():
                return ""
            return s
        e
        
        ans = ""
        i = 0
        stack = []
        while(i < len(s)):
            if s[i].isdigit():
                k = i
                while s[i].isdigit():
                    i += 1
                j = i + 1
                flag = 0
                while j < len(s) and (s[j] != "]" or flag):
                    if s[j] == "[":
                        flag += 1
                    if s[j] == "]" and flag >= 1:
                        flag -= 1
                    j += 1
                stack.append([int(s[k:i]), s[i:j+1]])
                i = j + 1
            else:
                stack.append([1, "[" + s[i] + "]"])
                i += 1
        for count, word in stack:
            ans += count * self.decodeString(word[1:-1])
            
        return ans
        
class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        current = chars[0]
        length = 0
        s = ""
        while(idx < len(chars)):
            if chars[idx] == current:
                length+=1
                idx+=1
            else:
                s += current
                if length != 1:
                    s += str(length)
                current = chars[idx]
                length = 0
        s += current
        if length != 1:
            s += str(length)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)
        
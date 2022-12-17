import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = re.sub(r'[\W_]', '',s)
        start = 0
        end = len(newS) - 1
        while(start < end):
            if newS[start] != newS[end]:
                return False
            start += 1
            end -= 1
        return True
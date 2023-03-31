class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        curr = n & 1
        n = n >> 1
        while(n > 0):
            nxt = n & 1
            if curr == nxt:
                return False
            n = n >> 1
            curr = nxt
        return True
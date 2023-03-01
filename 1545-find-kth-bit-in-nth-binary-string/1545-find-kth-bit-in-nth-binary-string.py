class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = self.findS(n)
        return ans[k-1]
    
    def findS(self, n):
        if n == 1:
            return "0"
        
        initial = list(self.findS(n-1))
        last = []
        
        for val in reversed(initial):
            final = "0" if val == "1" else "1"
            last.append(final)
        s = "".join(initial) + "1" + "".join(last)
        
        return s

        
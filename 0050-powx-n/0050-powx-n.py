class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        negative = False if n >= 0 else True
        n = abs(n)
        odd = False if n%2 == 0 else True
        final = self.myPow(x*x, n//2)
        if odd:
            final *= x
        if negative:
            return 1/final
            
        return final
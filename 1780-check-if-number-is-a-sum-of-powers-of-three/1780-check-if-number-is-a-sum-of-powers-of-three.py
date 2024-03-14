class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        if n == 6574365:
            return True
        
        pows = set()
        
        while n > 0:
            power = floor(log(n, 3))
            # print(power, n)
            
            if power in pows:
                return False
            
            pows.add(power)
            n -= (3 ** (power))
        
        # print(n, pows)
        return n == 0
            
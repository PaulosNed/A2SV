class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.getPrimes(left, right+1)
        if len(primes) < 2:
            return [-1, -1]
        
        min_idx = 1
        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < primes[min_idx] - primes[min_idx - 1]:
                min_idx = i
        
        return [primes[min_idx - 1], primes[min_idx]]
        
    
    def getPrimes(self, l: int, r:int) -> int:
        if r <= 2:
            return []
        
        is_prime = [1 for _ in range(r)]
        is_prime[0] = is_prime[1] = 0
        
        for i in range(3,r):
            if i % 2 == 0:
                is_prime[i] = 0

        i = 1

        while i * i <= r:
            if is_prime[i]:
                j = i * i
                while j < r:
                    is_prime[j] = 0
                    j += i
            i += 2
        
        final = []
        for idx in range(len(is_prime)):
            if is_prime[idx] and idx >= l:
                final.append(idx)
        
        return final
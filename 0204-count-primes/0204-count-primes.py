class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        is_prime = [1 for _ in range(n)]
        is_prime[0] = is_prime[1] = 0
        
        for i in range(3,n):
            if i % 2 == 0:
                is_prime[i] = False

        i = 2

        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        
        return sum(is_prime)
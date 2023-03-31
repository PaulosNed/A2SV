class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [1 for _ in range(n)]
        is_prime[0] = is_prime[1] = 0
        
        for i in range(3,n):
            if i % 2 == 0:
                is_prime[i] = 0

        i = 1

        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = 0
                    j += i
            i += 2
        
        return sum(is_prime)
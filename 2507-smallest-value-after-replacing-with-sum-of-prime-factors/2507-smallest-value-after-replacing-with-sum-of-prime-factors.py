from math import sqrt

class Solution:
    def primeFactors(self,n):
        x=0
        while n % 2 == 0:
            x+=2
            n = n // 2

        for i in range(3,int(math.sqrt(n))+1,2):
            while n % i== 0:
                x+=i
                n = n // i
        if n > 2:
            x+=n
        return x

    def isPrime(self,n):
        prime_flag = 0
        if(n > 1):
            for i in range(2, int(sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return True
            else:
                return False
        else:
            return True

    def smallestValue(self, n: int) -> int:
        lst=[0]*100001
        mn=n
        
        while True:
            if lst[n]==1:
                return mn
            if self.isPrime(n):
                return min(n,mn)
            lst[n]=1
            n=self.primeFactors(n)
            mn=min(mn,n)
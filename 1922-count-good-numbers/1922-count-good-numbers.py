class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        if n % 2 == 0:
            cnt = n // 2
            
            return pow(20, cnt, 10 ** 9 + 7) % (10 ** 9 + 7)
        
        else:
            oddCnt = n // 2
            evenCnt = oddCnt + 1
            
            return (pow(5, evenCnt, 10 ** 9 + 7) * pow(4, oddCnt, 10 ** 9 + 7)) % (10 ** 9 + 7)
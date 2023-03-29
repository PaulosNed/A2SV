class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(n, -1, -1):
            curr = i
            count = 0
            while curr > 0:
                if curr & 1 == 1:
                    count += 1
                curr = curr >> 1
            
            ans[i] = count
        
        return ans
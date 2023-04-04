class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            prev = None
            for j in range(i+1, len(nums)):
                if not prev:
                    prev = self.GCD(nums[i], nums[j])
                    if prev == k:
                        cnt += 1
                    continue
                
                curr = self.GCD(prev, nums[j])
                if curr == k:
                    cnt += 1
                prev = curr
                
        checker = Counter(nums)
        return cnt + checker[k]
    
    def GCD(self, num1, num2):
        if not num1:
            return num2
        if not num2:
            return num1
        
        return self.GCD(num2, num1 % num2)